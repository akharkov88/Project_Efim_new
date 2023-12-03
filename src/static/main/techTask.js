$(document).ready(function () {
    console.log("ready!");

});
$("button:contains('Добавить новое задание')").on("click", function () {

    console.log(111)
    window.location.href = "/main/techTaskForm.html"

})
// $('button:contains("Изменить")').on("click", function () {
//     console.log(222)
// })
