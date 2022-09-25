

// csrftoken: exist from register.js file

// login form
var login_form = document.getElementById('login_form')


// action when submit the form
login_form.addEventListener('submit', function (e){
    e.preventDefault()
    url = 'http://localhost:8000/account/token/'

    user = {'username': login_form.username.value,
        'password':login_form.password.value,
        }

	var requestOptions = {
		  method: 'POST',
		  headers:  {
			  'Accept': 'application/json',
			  "Content-Type": "application/json",
			  'X-CSRFToken':csrftoken,
		  },
		  body: JSON.stringify(user), // convert to json

	};


	fetch(url, requestOptions)
	  .then(response => response.text())
	  .then(function (res){
		  try{
			  window.atob(JSON.parse(res).access.split('.')[1])
			  sessionStorage.setItem('token', res);

			  storeTokenInDjangoSession()

			  location.replace("http://localhost:6123/");


		  }catch(e){
			  console.log('You should enter correct username and password')
		  }

	  }
	  )
	  .catch(error => console.log('error', error));


})



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