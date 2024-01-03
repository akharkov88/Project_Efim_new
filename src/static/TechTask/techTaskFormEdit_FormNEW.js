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
            $("#tetst_v").empty();
            for (var i in ingredients) {
                $("<option/>").html(ingredients[i].value_table).appendTo("#tetst_v");
            }
        }
    });
}

$("#input_v").on("keyup", function (event) {
    var _this = $(this);
    var value = _this.val();
    set_options_datalist("type", value, 5)
});
$(document).on('change', 'input', function() {
  var options = $('datalist')[0].options;
  var val = $(this).val();
  for (var i = 0; i < options.length; i++) {
    if (options[i].value === val) {
      console.log("Выбрали значения",val);
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

