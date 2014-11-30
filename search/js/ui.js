// $('input[name=toggle]').defaultChecked;
document.getElementById("regex").style.color = "#8D8D8D";

$('input[name=toggle]').change(function(){

    if($(this).is(':checked'))
    {
        document.getElementById("search").style.backgroundColor = "#FFC800";
        document.getElementById("searchField").style.color = "#FFC800";
        document.getElementById("keyword").style.color = "#FFC800";
        document.getElementById("regex").style.color = "#8D8D8D";
        $( ".circle:before" ).css( "background-color", "#8D8D8D");
        $(".spinner").removeClass("blue");
        $(".spinner").addClass("yellow");
    }
    else
    {
        document.getElementById("search").style.backgroundColor = "#4AAAE1";
        document.getElementById("searchField").style.color = "#4AAAE1";
        document.getElementById("regex").style.color = "#4AAAE1";
        document.getElementById("keyword").style.color = "#8D8D8D";
        $(".spinner").addClass("blue");
        $(".spinner").removeClass("yellow");
    }    

});