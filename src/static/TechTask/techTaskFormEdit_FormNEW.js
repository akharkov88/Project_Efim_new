$("#div1").delegate(":input", "input", function (e) {
    var options = $('datalist')[0].options;
    if (options.length != 0 && options[options.length - 1].value == $(this).val()) {
        if ($(this).val().indexOf("Добавить в список \"") != -1) {
            set_setSuggest("type", $(this).val().replace("Добавить в список \"", "").slice(0, -1),"tetst_v")
            $('#input_v').val($(this).val().replace("Добавить в список \"", "").slice(0, -1));
        }
        return
    }
    set_options_datalist("type", e.target.value,"tetst_v", 5)

});

function set_options_datalist(customer_id, search,id_datalist, count = 10) {
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

                console.log("search",search)
                console.log("ingredients[i].value_table",ingredients[i].value_table)

                if (ingredients[i].value_table == search) {
                console.log("return")

                    return
                }
            }
                console.log("return2")

            $(`#${id_datalist}`).empty();
            for (var i in ingredients) {
                $(`<option id="${i}" />`).html(ingredients[i].value_table).appendTo(`#${id_datalist}`);
                if (i == ingredients.length - 1) {
                    $(`<option/>`).html(`Добавить в список "${search}"`).appendTo(`#${id_datalist}`);
                }

            }
        },
        error: function (error) {
            $(`#${id_datalist}`).empty();
            $(`<option/>`).html(`Добавить в список "${search}"`).appendTo(`#${id_datalist}`);

        },
    });
}

function set_setSuggest(customer_id, add_value,id_datalist) {
    $.ajax({
        method: 'POST',
        url: "/suggest/setSuggest",
        headers: {
            Accept: 'application/json',
            'Content-Type': 'application/json',
            "Authorization": localStorage.getItem('Authorization')
        },
        data: `{"customer_id":"${customer_id}","value_table": "${add_value}"}`,
        success: function (ingredients) {
            $(`#${id_datalist}`).empty();

            set_options_datalist("type",add_value,5)

        },
        error: function (error) {
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

