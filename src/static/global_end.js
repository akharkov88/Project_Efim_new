

document.getElementById('adminMenu').onclick = async function (event) {
    console.log('adminMenu')
    check_user = await fetch('/auth/user/', {
        headers: {
            Accept: 'application/json',
            "Authorization": getCookieValue("Authorization")
        },
    });
    let responseText = await check_user.text();
    console.log("1responseText",responseText)

    console.log("2responseText",JSON.parse(responseText).roles)
    console.log("3responseText",JSON.parse(JSON.parse(responseText).roles).indexOf("Admin"))
    if (check_user.status == 200 && JSON.parse(JSON.parse(responseText).roles).indexOf("Admin")!=-1) {
    console.log("check_user.status",check_user.status)
        document.location.href = '/main/adminMenu'

    }
}



document.getElementById('Logout').onclick = async function (event) {
    deleteCookie("Authorization")
        document.location.href = '/auth'

}
