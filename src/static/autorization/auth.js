function autorization(){
alert('123й4')
}

 addEventListener("submit", async(event) => {

    console.log('1')
    console.log(event)

        event.preventDefault();

    let response = await fetch('/article/formdata/post/user', {
      method: 'POST',
      body: new FormData(document.getElementById("formElem")
)
    });

    let result = await response.json();

    console.log(result.message);

});
