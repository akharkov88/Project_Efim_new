document.getElementById('adminMenu').onclick = async function (event) {
    console.log('adminMenu')
    check_user = await fetch('/auth/user/', {
        headers: {
            Accept: 'application/json',
            "Authorization": getCookieValue("Authorization")
        },
    });
    let responseText = await check_user.text();
    console.log("1responseText", responseText)

    console.log("2responseText", JSON.parse(responseText).roles)
    console.log("3responseText", JSON.parse(JSON.parse(responseText).roles).toLowerCase().indexOf("admin"))
    if (check_user.status == 200 && JSON.parse(JSON.parse(responseText).roles).toLowerCase().indexOf("admin") != -1) {
        console.log("check_user.status", check_user.status)
        document.location.href = '/main/adminMenu'

    }
}

async function get_my_UserPfofile(event) {

    return get_my_UserPfofile
}


document.getElementById('Logout').onclick = async function (event) {
    deleteCookie("Authorization")
    document.location.href = '/auth'

}

async function get_UserTask_global() {
    check_user = await fetch('/auth/get_my_UserPfofile/', {
        headers: {
            Accept: 'application/json',
            "Authorization": getCookieValue("Authorization")
        },
    });
    window.my_UserPfofile = JSON.parse(await check_user.text());
    res = await fetch('/userprofile/get_UserTask', {
        headers: {
            Accept: 'application/json',
            "Authorization": getCookieValue("Authorization")
        },
    });
    let responseText = await res.text();
    zadachi_no_work = 0
    zadachi_in_work = 0
    department_task = 0
    if (res.status == 200) {
        Header_show_value = 0

        list_task = JSON.parse(responseText)
        console.log("list_task", list_task)
        for (v of list_task) {

            if (v.status == "Назначена" && JSON.parse(v.user_executor.split("'").join('"')).indexOf(window.my_UserPfofile.my_username) != -1) {
                zadachi_no_work++
            }

            if (v.status == "В Работе" && JSON.parse(v.user_executor.split("'").join('"')).indexOf(window.my_UserPfofile.my_username) != -1) {
                zadachi_in_work++
            }


            if (v.status == "Назначена" || v.status == "В Работе") {
                for (UserPfofile of v.UserPfofile_executor) {
                    if (UserPfofile.department == window.my_UserPfofile.department) {

                        department_task++
                        break
                    }

                }
            }


            if (v.notification_executor == true) {
                Header_show_value++
            }
        }
        document.getElementById("Header_show").innerHTML = '<i class="fa fa-bell fa-fw"></i>' + Header_show_value
        if (document.getElementById("zadachi_no_work")) {
            document.getElementById("zadachi_no_work").innerText = zadachi_no_work
        }
        if (document.getElementById("zadachi_in_work")) {
            document.getElementById("zadachi_in_work").innerText = zadachi_in_work
        }
        if (document.getElementById("department_task")) {
            document.getElementById("department_task").innerText = department_task
        }


    }
}

get_UserTask_global()