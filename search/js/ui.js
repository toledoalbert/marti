// $('input[name=toggle]').defaultChecked;
$("#spinner").hide();
document.getElementById("regex").style.color = "#8D8D8D";

$('input[name=toggle]').change(function(){

    if($(this).is(':checked'))
    {
        $("#search").addClass("keyword");
        $("#search").removeClass("regex");
        document.getElementById("searchField").style.color = "#FFC800";
        document.getElementById("keyword").style.color = "#FFC800";
        document.getElementById("regex").style.color = "#8D8D8D";
        $( ".circle:before" ).css( "background-color", "#8D8D8D");
        $(".spinner").removeClass("blue");
        $(".spinner").addClass("yellow");
        $(".logo").addClass("keyword");
        $(".logo").removeClass("regex");
    }
    else
    {
        $("#search").addClass("regex");
        $("#search").removeClass("keyword");
        document.getElementById("searchField").style.color = "#4AAAE1";
        document.getElementById("regex").style.color = "#4AAAE1";
        document.getElementById("keyword").style.color = "#8D8D8D";
        $(".spinner").addClass("blue");
        $(".spinner").removeClass("yellow");
        $(".logo").removeClass("keyword");
        $(".logo").addClass("regex");
    }    

});