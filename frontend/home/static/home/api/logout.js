
function logout(){
    sessionStorage.setItem('token', null)
    storeTokenInDjangoSession()
    window.location.replace("http://localhost:6123/registration");

}