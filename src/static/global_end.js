


document.getElementById('Settings Create_User').onclick = function (event) {
    check_user = fetch('/auth/user/', {
        headers: {
            Accept: 'application/json',
            "Authorization": localStorage.getItem('Authorization')
        },
    });
    if (check_user.status != 200) {
        document.location.href = '/auth/create'
    }

}

