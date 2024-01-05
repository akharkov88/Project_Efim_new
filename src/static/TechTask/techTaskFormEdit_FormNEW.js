function set_options_datalist(customer_id, search, count = 10) {
    $.ajax({
        method: 'POST',
        url: "/suggest/getSuggest",
        headers: {
            Accept: 'application/json',
            'Content-Type': 'application/json',
            "Authorization": localStorage.getItem('Authorization')
        },
        data: `{"customer_id":"${customer_id}","search": "${search}","count":${count}}`,
        success: function (ingredients) {
            for (var i in ingredients) {
                if (ingredients[i].value_table == search) {
                    return
                }
            }
            // ingredients.unshift({value_table:"Добавить значение в список"})

            console.log("ingredients",ingredients)
            $("#tetst_v").empty();
                // $("<option/>").html("Добавить значение в список"+i).appendTo("#tetst_v");

            for (var i in ingredients) {
                $("<option/>").html(ingredients[i].value_table).appendTo("#tetst_v");
            }

            console.log("111111111111111111111")

        },

              error: function (error) {

                   console.log("error",error)
                // $("<option/>").html("Добавить значение в список").appendTo("#tetst_v");


      },
      // complete: function () {
      //   // Handle the complete event
      //   alert("ajax completed " + cartObject.productID);
      // }

    });
}

$("#input_v").on("keyup", function (event) {
    var _this = $(this);
    var value = _this.val();
    console.log("value", value)

    set_options_datalist("type", value, 5)
    // _this.removeAttr("list").focus();


});
$(document).on('change', 'input', function (event) {
    console.log("change")

    var _this = $(this);
    var options = $('datalist')[0].options;
    var val = $(this).val();
    for (var i = 0; i < options.length; i++) {
        if (options[i].value === val) {
            console.log("Выбрали значения", val);
            $("#tetst_v").blur()
//         _this.removeAttr("list").focus();
// setTimeout(function() {
//     document.getElementById('input_v').setAttribute('list', document.getElementById('tetst_v').id);
// },100);
            break;
        }
    }
});
// functi
// async function fff() {
//     let response = await fetch('/suggest/getSuggest', {
//         headers: {
//             Accept: 'application/json',
//             'Content-Type': 'application/json',
//             "Authorization": localStorage.getItem('Authorization'),
//             // "Content-Type": 'application/x-www-form-urlencoded'
//         },
//         method: 'POST',
//         // body: `grant_type=&username=${document.getElementById("login").value}&password=${document.getElementById("password").value}&scope=&client_id=&client_secret=`
//         body: `{"customer_id":"string","count":0}`
//     });
//     let result = await response.json();
//     console.log("result", result)
//
//     if (response.status == 200) {
//         console.log("200")
//     }
// }

