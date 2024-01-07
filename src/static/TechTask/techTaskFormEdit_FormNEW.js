$("#div1").delegate(":input", "input", function (e) {
    var options = $('datalist')[0].options;
    if (options.length!=0 && options[options.length-1].value==$(this).val()){
        return
    }
    set_options_datalist("type", e.target.value, 5)

});
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
            $("#tetst_v").empty();
            for (var i in ingredients) {
                $(`<option id="${i}" />`).html(ingredients[i].value_table).appendTo("#tetst_v");
                if (i == ingredients.length - 1) {
                    $(`<option/>`).html(search).appendTo("#tetst_v");
                }

            }
        },
        error: function (error) {
            $("#tetst_v").empty();
            $(`<option/>`).html(search).appendTo("#tetst_v");

        },
    });
}
//
// $("#input_v").delegate(":input", "input", function (event) {
//     var _this = $(this);
//     var value = _this.val();
//     console.log("value", value)
//
//     set_options_datalist("type", value, 5)
//     // _this.removeAttr("list").focus();
//
//
// });
// $(document).on('change', 'input', function (event) {
//     console.log("change")
// })
//
// $(document).on( 'change', function() {
//     console.log("change")
//
// })
// $(document).on( 'input', function() {
//     console.log("change")
//
// })
//     var options = $('datalist')[0].options;
//     if (options[options.length-1].value==$(this).val()){
//     }


//         _this.removeAttr("list").focus();
// setTimeout(function() {
//     document.getElementById('input_v').setAttribute('list', document.getElementById('tetst_v').id);
// },100);
// });
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

