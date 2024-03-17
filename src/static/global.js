if(typeof(String.prototype.trim) === "undefined")
{
    String.prototype.trim = function()
    {
        return String(this).replace(/^\s+|\s+$/g, '');
    };
}

async function send_telegram(user,text) {

    res = await fetch('/message/Telegram_send_message', {
        method:"POST",
        headers: {
            Accept: 'application/json',
            'Content-Type': 'application/json',
        },
        body:JSON.stringify(
            {
  "User": user,
  "Value": text
})
    });
    let responseText = await res.text();
            console.log("res.status",res.status)

    if (res.status == 200) {
        console.log(responseText)
    }
}

// send_telegram("admin", "getwiki(command)")

async function send_telegram_group(text) {

    res = await fetch('/message/Telegram_send_message_group', {
        method:"POST",
        headers: {
            Accept: 'application/json',
            'Content-Type': 'application/json',
        },
        body:JSON.stringify(
            {
  "Value": text
})
    });
    let responseText = await res.text();
            console.log("res.status",res.status)

    if (res.status == 200) {
        console.log(responseText)
    }
}

// send_telegram_group( "Проверка")


async function check_user_func() {
    console.log("check_user_func")
    console.log("check_user_func", getCookieValue("Authorization"))
    check_user = await fetch('/auth/user/', {
        headers: {
            Accept: 'application/json',
            "Authorization": getCookieValue("Authorization")
        },
    });
    console.log("check_user_func", check_user.status)

    if (check_user.status != 200) {
        document.location.href = '/auth/'
    }
}

check_user_func()

async function autroriz() {
    // if (window.stop !== undefined) {
    //     window.stop();
    // } else if (document.execCommand !== undefined) { // для IE
    //     document.execCommand("Stop", false);
    // }

    //works in all browsers but IE
    // if ($.browser.msie) {
    //     document.execCommand("Stop");
    // }    ;

    if (sessionStorage.getItem('stopload')) { // если в хранилище есть переменная 'stopload'
        // sessionStorage.removeItem('stopload'); // удалить 'stopload' из хранилища
    } else { // остановить загрузку HTML страницы
        if (window.stop !== undefined) {
            window.stop();
        } else if (document.execCommand !== undefined) {
            document.execCommand("Stop", false);
        }
    }
    check_user = await fetch('/auth/user/', {
        headers: {
            Accept: 'application/json',
            "Authorization": getCookieValue("Authorization")
        },
    });
// debugger


    console.log("check_user.status", check_user.status)
    if (check_user.status != 200) {

        document.location.href = '/auth/'
    } else {
        console.log("check_user.status", check_user.status)

        if (sessionStorage.getItem('stopload')) { // если в хранилище есть переменная 'stopload'
            sessionStorage.removeItem('stopload');
        } else {
            sessionStorage.setItem('stopload', 'none'); // занести переменную в хранилище

            location.reload();
        }

    }
} // функция останавливает загрузку страницы


function downloadFileFromURL(url, fileName) {
    const xhr = new XMLHttpRequest();
    xhr.open('GET', url, true);
    xhr.responseType = 'blob';

    xhr.onload = function () {
        if (xhr.status === 200) {
            const blob = new Blob([xhr.response]);
            const link = document.createElement('a');
            link.href = URL.createObjectURL(blob);
            link.download = fileName;
            link.click();
        } else {
            console.error('Error downloading file:', xhr.statusText);
        }
    };

    xhr.send();
}

async function check_user_Admin() {
    if (window.location.pathname == '/main/adminMenu') {
        check_user = await fetch('/auth/user/', {
            headers: {
                Accept: 'application/json',
                "Authorization": getCookieValue("Authorization")
            },
        });
        let responseText = await check_user.text();
        console.log("222222", JSON.parse(JSON.parse(responseText).roles).indexOf("Admin"))
        if (JSON.parse(JSON.parse(responseText).roles).indexOf("Admin") == -1) {
            document.location.href = '/main'
        }
    }

}

check_user_Admin()


async function check_menu_Admin() {
    check_user = await fetch('/auth/user/', {
        headers: {
            Accept: 'application/json',
            "Authorization": getCookieValue("Authorization")
        },
    });
    let responseText = await check_user.text();
    if (JSON.parse(JSON.parse(responseText).roles).indexOf("Admin") == -1) {
        showStuff("adminMenu")
    }

}

function showStuff(id) {
    console.log("showStuffshowStuff")
    document.getElementById(id).style.display = 'block';
    // hide the lorem ipsum text
    document.getElementById(id).style.display = 'none';
    // hide the link
    // btn.style.display = 'none';
}

check_menu_Admin()


function getCookieValue(name) {
    const regex = new RegExp(`(^| )${name}=([^;]+)`)
    const match = document.cookie.match(regex)
    if (match) {
        return match[2]
    }
}

function setCookie(name, value, options = {}) {

    options = {
        path: '/',
        // при необходимости добавьте другие значения по умолчанию
        ...options
    };

    if (options.expires instanceof Date) {
        options.expires = options.expires.toUTCString();
    }

    let updatedCookie = encodeURIComponent(name) + "=" + encodeURIComponent(value);

    for (let optionKey in options) {
        updatedCookie += "; " + optionKey;
        let optionValue = options[optionKey];
        if (optionValue !== true) {
            updatedCookie += "=" + optionValue;
        }
    }

    document.cookie = updatedCookie;
}

// Пример использования:
// setCookie('user', 'John', {secure: true, 'max-age': 3600});
function deleteCookie(name) {
    setCookie(name, "", {
        'max-age': -1
    })
}


function validForm_global(elements) {
    // let elements = $('form').serializeArray();
    valid = true
    for (let key of elements) {
        if (key.value == '') {
            valid = false
            document.getElementsByName(key.name)[0].setAttribute("required", true)
        } else {
            document.getElementsByName(key.name)[0].removeAttribute("required")
        }
    }


    return valid
}

function removeOptions(selectElement) {
    while (selectElement.options.length > 0) {
        selectElement.remove(0);
    }
}

