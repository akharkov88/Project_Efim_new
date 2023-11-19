
 addEventListener("submit", async(event) => {

    console.log('1')
    console.log(event)
    event.preventDefault();
    // let response = await fetch('/auth/sign-in/', {
    // headers: {
    // Accept: 'application/json',
    // "Content-Type": 'application/x-www-form-urlencoded'
    //     },
    // method: 'POST',
    // body: `grant_type=&username=${document.getElementById("login").value}&password=${document.getElementById("password").value}&scope=&client_id=&client_secret=`
    // });
    // let result = await response.json();
    // if (response.status==200){
    //     window.location.pathname = '/main'
    // }

        let response = await fetch('/auth/sign-in/', {
    headers: {
    Accept: 'application/json',
    "Content-Type": 'application/x-www-form-urlencoded'
        },
    method: 'POST',
    body: `grant_type=&username=${document.getElementById("login").value}&password=${document.getElementById("password").value}&scope=&client_id=&client_secret=`
    });
    let result = await response.json();
   console.log(result)
     // document.cookie = "Authorization" + '=' + result.token_type+" "+result.access_token;
     // document.cookie = "Authorization="+result.token_type+" "+result.access_token;
     // document.cookie = "Cookie="+result.token_type+" "+result.access_token;
     // document.cookie = "Bearer "+result.access_token;
     // document.cookie = result.token_type+" "+result.access_token;
// document.location.href ='/main/'
//          if (response.status==200){
        // window.location.pathname = '/main'
        // document.location.href ='/main/'
        //      return window.location.href = "/main/";
    // }
    //  response2 = await fetch('/main/', {
    // headers: {
    // Accept: 'application/json',
    // "Authorization": result.token_type+" "+result.access_token
    //     },
    // });
    //
    //  result2 = await response2;
    //  console.log("result2",result2.text())
    //      if (response2.status==200) {
    //
    //          document.querySelector('html').innerHTML = response2.text()
    //      }
//      var html = document.getElementByTagName('html');
// html.innerHTML = 'Изменено';
// document.location.href ='/main/'

     fetch('/main/',{
    headers: {
    Accept: 'application/json',
    "Authorization": result.token_type+" "+result.access_token
        },
    })
    .then(function(response) {
        // When the page is loaded convert it to text
        return response.text()
    })
    .then(function(html) {
        // Initialize the DOM parser
        var parser = new DOMParser();

        // Parse the text
        var doc = parser.parseFromString(html, "text/html");

        // You can now even select part of that html as you would in the regular DOM
        // Example:
        // var docArticle = doc.querySelector('article').innerHTML;

        console.log(doc);
        document.querySelector('html').innerHTML =html
        // document.body.innerHTML = html
    })
    .catch(function(err) {
        console.log('Failed to fetch page: ', err);
    });


    //  fetch('/main/')
    // .then(function(response) {
    //     // When the page is loaded convert it to text
    //     return response.text()
    // })
    // .then(function(html) {
    //     // Initialize the DOM parser
    //     var parser = new DOMParser();
    //     // Parse the text
    //     var doc = parser.parseFromString(html, "text/html");
    //     // You can now even select part of that html as you would in the regular DOM
    //     // Example:
    //     // var docArticle = doc.querySelector('article').innerHTML;
    //     console.log(doc);
    //
    //     document.querySelector('html').innerHTML =String(doc)
    // })
    // .catch(function(err) {
    //     console.log('Failed to fetch page: ', err);
    // });

});
