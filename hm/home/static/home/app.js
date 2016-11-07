var main;
main = function () {

    $("#myBtn").click(function () {
        $("#id_user_id").val("");
        $("#id_password").val("");
        $("#myModal").modal();
    });

    $("#hostel-dd").hover(function () {
            $('#hostel-menu').stop(true, true).fadeIn("fast");
            $(this).toggleClass('open');
            $('#h-c').toggleClass("caret caret-up");
        },
        function () {
            $('#hostel-menu').stop(true, true).fadeOut("slow");
            $(this).toggleClass('open');
            $('#h-c').toggleClass("caret caret-up");

        });

    $("#user-dd").hover(function () {
            $('#user-menu').stop(true, true).fadeIn("fast");
            $(this).toggleClass('open');
            $('#u-c').toggleClass("caret caret-up");
        },
        function () {
            $('#user-menu').stop(true, true).fadeOut("slow");
            $(this).toggleClass('open');
            $('#u-c').toggleClass("caret caret-up");

        });

    $(document).scroll(function () {
        var y = $(this).scrollTop();
        var x = $("#nav").position();
        if (y > x.top) {
            $('#nav').addClass('sticky');

        } else {
            $('#nav').removeClass('sticky');

        }

    });

    $('#respon').click(function () {
        var x = document.getElementById("myTopnav");
        if (x.className === "menu") {
            x.className += " responsive";
        } else {
            x.className = "menu";
        }
    });

    $('#nav li a').on('click', function () {
        $(this).parent().parent().find('.active').removeClass('active');
        $(this).parent().addClass('active');
    });

    $(".compBtn").click(function () {
        var a = $(this).attr("id");
        $("#complaintType").text(a);
        $("#complModal").modal();
    });



    $('.carousel').carousel({
        interval: 1500
    });

};

$(document).ready(main);