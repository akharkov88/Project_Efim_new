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
