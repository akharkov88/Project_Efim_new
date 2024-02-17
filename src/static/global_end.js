

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
async function get_UserTask_global() {

    res = await fetch('/userprofile/get_UserTask', {
        headers: {
            Accept: 'application/json',
            "Authorization": getCookieValue("Authorization")
        },
    });
    let responseText = await res.text();
            console.log("res.status",res.status)

    if (res.status == 200) {
        Header_show_value = 0
        for (v of JSON.parse(responseText)) {
            // console.log(v.notification_executor)
            if (v.notification_executor == true) {
                Header_show_value++
            }
        }
        document.getElementById("Header_show").innerHTML = '<i class="fa fa-bell fa-fw"></i>' + Header_show_value
    }
}

get_UserTask_global()