// read cookies
function getCookie(name) {
		    var cookieValue = null;
		    if (document.cookie && document.cookie !== '') {
		        var cookies = document.cookie.split(';');
		        for (var i = 0; i < cookies.length; i++) {
		            var cookie = cookies[i].trim();
		            // Does this cookie string begin with the name we want?
		            if (cookie.substring(0, name.length + 1) === (name + '=')) {
		                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
		                break;
		            }
		        }
		    }
		    return cookieValue;
		}

// crsf
var csrftoken = getCookie('csrftoken');

// get token from storage
function getToken(){
    return JSON.parse(sessionStorage.getItem('token'))
}

// decode the token parts
function parseJwt (token) {
    var base64Url = token.split('.')[1];
    var base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
    var jsonPayload = decodeURIComponent(window.atob(base64).split('').map(function(c) {
        return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
    }).join(''));

    return JSON.parse(jsonPayload);
}

// check if the access or refresh is expired
function isExpired(token_part){
      const expiry = token_part.exp;
      const now = new Date();
      return now.getTime() >= expiry * 1000;
}

// check if the refresh token is expired then return false
// else remake new access token and save it in the sessionStorage
// en: encoding token
// de: decoding token
function refreshToken(refresh_en, refresh_de){
    if (isExpired(refresh_de))
        return false

    url = 'http://localhost:8000/account/token/refresh/'

    refresh_dir = {'refresh': refresh_en}


	var requestOptions = {
		  method: 'POST',
		  headers:  {
			  'Accept': 'application/json',
			  "Content-Type": "application/json",
			  'X-CSRFToken':csrftoken,
		  },
		  body: JSON.stringify(refresh_dir),

	};

	fetch(url, requestOptions)
	  .then(response => response.text())
	  .then(function (res){
          new_access_en = JSON.parse(res)['access'] // api return access as json
		  sessionStorage.setItem('token',
              JSON.stringify(
                  {
                  'access': new_access_en,
                  'refresh': refresh_en,
                  }
              ));
	  }
	  )
	  .catch(error => console.log('error', error));

    storeTokenInDjangoSession()
    return true
}

// for check if the user still authenticated or not
function isAuth(){
    try{
        token = getToken()
        // if there is no any token
        if (token == null)
            return false
        // decode the access token
        access_de = parseJwt(token['access'])

        refresh_en = token['refresh']
        // decode the refresh token
        refresh_de = parseJwt(refresh_en)

        // check the expired for bot access and refresh token
        if (isExpired(access_de)) {
            if (!refreshToken(refresh_en, refresh_de)) {
                return false
            }
        }
        return true
    }catch (e){
        return false
    }
}

window.onload = function() {


    if (!isAuth()){
    logout()
    }
}

function storeTokenInDjangoSession(){

    url = 'http://localhost:6123/store_token/'

    fetch(url, {
				method:'POST',
				headers:{
				    'Accept': 'application/json',
					'Content-type':'application/json',
					'X-CSRFToken':csrftoken,
				},
				body: sessionStorage.getItem('token')
			}
			).then(function(response){
				console.log('token saved')
			})


}