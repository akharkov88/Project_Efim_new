async function check_user_func() {

    check_user = await fetch('/auth/user/', {
        headers: {
            Accept: 'application/json',
            "Authorization": localStorage.getItem('Authorization')
        },
    });
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
            "Authorization": localStorage.getItem('Authorization')
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
        }else {
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

