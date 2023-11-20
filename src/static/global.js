async function  check_user_func  (){
    check_user=  await fetch('/auth/user/', {
    headers: {
    Accept: 'application/json',
    "Authorization": localStorage.getItem('Authorization')
    },
});
    if (check_user.status!=200){
     document.location.href ='/auth/'
    }
}
check_user_func()