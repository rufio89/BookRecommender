/**
 * Created by ryan on 5/28/17.
 */
$(document).ready(function(){
    bindFuncs();
})

var loader = "<div class='ui active centered inline loader'></div>";

function bindFuncs(){
    getSearchResults();
    autoComplete();
}

function getSearchResults(){
    $('#btn-search').on('click', function(){
        $("#results").html(loader);
        var isbn = $("#book-search").attr("data-isbn");
        //alert(isbn);
        getBookDetail(isbn);
    });

    $('#book-search').on('keyup', function(e) {
        if(e.which == 13) {
            $("#results").html(loader);
            var isbn = $("#book-search").attr("data-isbn");
            //alert(isbn);
            getBookDetail(isbn);
        }
    });

}

function getBookDetail(isbn){
    $.ajax({
        url: '/books/detail/' + isbn.toString(),
        type: "GET",
        success: function(response) {
            console.log(response);
            $("#results").html();
            $("#results").html(response);
        }
    });
}

function autoComplete() {
    $(function () {
        $("#book-search").autocomplete({
            source: "/books/lookup/",
            select: function(event, ui) {
                event.preventDefault();
                $("#book-search").val(ui.item.label);
                $('#book-search').attr("data-isbn",ui.item.value);
            },
            focus: function(event, ui) {
                event.preventDefault();
                $("#book-search").val(ui.item.label);
            },
            minLength: 4,
        });
    });

}