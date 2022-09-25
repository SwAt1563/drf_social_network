
// function for get the cookie by name
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

// register form
var register_form = document.getElementById('register_form')

// action when submit
register_form.addEventListener('submit', function (e){
    e.preventDefault()
    url = 'http://localhost:8000/account/register/'


    new_user = {'username': register_form.username.value,
        'email':register_form.email.value,
        'password':register_form.password.value,
        'password2':register_form.password2.value}

    fetch(url, {
				method:'POST',
				headers:{
				    'Accept': 'application/json',
					'Content-type':'application/json',
					'X-CSRFToken':csrftoken,
				},
				body:JSON.stringify(new_user) // convert to json
			}
			).then(function(response){
				location.replace("http://localhost:6123/registration/")
			})
})
