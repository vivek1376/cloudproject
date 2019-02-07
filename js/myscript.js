document.addEventListener("DOMContentLoaded", function() {
    document.querySelector('input#submit').addEventListener("click", function () {
        var l = document.querySelector('select#genrelist');
        var lval = l.options[l.selectedIndex].text;

        var yr = document.querySelector('input#yearbox').value;

        aja()
            .method('POST')
            .url('/')
            .timeout(2500)
            .data({'val1': lval,'val2': yr})
            .on('200', function (response) {
                console.log('ajax response received!!' + JSON.stringify(response));
            })
            .go();
        console.log("clicked");
    });
});