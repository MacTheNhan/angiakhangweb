var h = document.getElementById("col-r").offsetHeight;
document.getElementById("col-l").style.height = h + "px";

// news
var curPos1 = 1;
var timer1 = setTimeout("Slidenews(1)", 9000);

function Slidenews(index1) {
    clearTimeout(timer1);

    document.getElementById("itm-news" + curPos1).style.display = "none";
    document.getElementById("itm-news" + index1).style.display = "";

    curPos1 = index1;
    index1 = (index1 == 5) ? 1 : (index1 + 1);
    timer1 = setTimeout("Slidenews(" + index1 + ")", 9000);
}

$(function () {

    var filterList = {
        init: function () {
            $('#portfoliolist').mixitup({
                targetSelector: '.portfolio',
                filterSelector: '.filter',
                effects: ['fade'],
                easing: 'snap',
                onMixEnd: filterList.hoverEffect()
            });
        },
        hoverEffect: function () {
            $('#portfoliolist .portfolio').hover(
                function () {
                    $(this).find('.label').stop().animate({
                        bottom: 0
                    }, 200, 'easeOutQuad');
                    $(this).find('img').stop().animate({
                        top: 0
                    }, 500, 'easeOutQuad');
                },
                function () {
                    $(this).find('.label').stop().animate({
                        bottom: -90
                    }, 200, 'easeInQuad');
                    $(this).find('img').stop().animate({
                        top: 0
                    }, 300, 'easeOutQuad');
                }
            );
        }
    };
    filterList.init();
});


$(document).ready(function () {
    var owl = $("#portfoliolist");

    owl.owlCarousel({
        items: 4,
        navigation: true,
        pagination : false,
        navigationText: ["<span class='glyphicon glyphicon-chevron-left' aria-hidden='true'></span>", "<span class='glyphicon glyphicon-chevron-right' aria-hidden='true'></span>"],
        itemsCustom: [
            [0, 1],
            [450, 1],
            [600, 2],
            [700, 3],
            [1000, 5],
            [1200, 5],
            [1400, 5],
            [1600, 5]
        ]

    });


    $('.modal').each(function () {
        var src = $(this).find('iframe').attr('src');

        $(this).on('click', function () {

            $(this).find('iframe').attr('src', '');
            $(this).find('iframe').attr('src', src);

        });
    });

    // youtube play
    autoPlayYouTubeModal();


    var owl = $("#owl-demo");
    owl.owlCarousel({
        autoHeight: false,
        items: 3,
        itemsCustom: [
            [0, 1],
            [450, 1],
            [600, 2],
            [700, 3],
            [1024, 3],
            [1200, 3],
            [1400, 3],
            [1600, 3]
        ]
    });


    var owl = $("#owl-demo4");

    owl.owlCarousel({
        items: 4,
        itemsCustom: [
            [0, 1],
            [450, 1],
            [600, 2],
            [700, 3],
            [1000, 5],
            [1200, 5],
            [1400, 5],
            [1600, 5]
        ]

    });

});


//FUNCTION TO GET AND AUTO PLAY YOUTUBE VIDEO FROM DATATAG
function autoPlayYouTubeModal() {
    var trigger = $("body").find('[data-toggle="modal"]');
    trigger.click(function () {
        var theModal = $(this).data("target"),
            videoSRC = $(this).attr("data-theVideo"),
            videoSRCauto = videoSRC + "?autoplay=1";
        $(theModal + ' iframe').attr('src', videoSRCauto);
        $(theModal + ' button.close').click(function () {
            $(theModal + ' iframe').attr('src', videoSRC);
        });
    });
}

// Landmark 81
jssor_1_slider_init = function () {

    var jssor_1_SlideoTransitions = [
        [{ b: 0, d: 600, y: -290, e: { y: 27 } }],
        [{ b: 0, d: 1000, y: 185 }, { b: 1000, d: 500, o: -1 }, { b: 1500, d: 500, o: 1 }, { b: 2000, d: 1500, r: 360 }, { b: 3500, d: 1000, rX: 30 }, { b: 4500, d: 500, rX: -30 }, { b: 5000, d: 1000, rY: 30 }, { b: 6000, d: 500, rY: -30 }, { b: 6500, d: 500, sX: 1 }, { b: 7000, d: 500, sX: -1 }, { b: 7500, d: 500, sY: 1 }, { b: 8000, d: 500, sY: -1 }, { b: 8500, d: 500, kX: 30 }, { b: 9000, d: 500, kX: -30 }, { b: 9500, d: 500, kY: 30 }, { b: 10000, d: 500, kY: -30 }, { b: 10500, d: 500, c: { x: 87.50, t: -87.50 } }, { b: 11000, d: 500, c: { x: -87.50, t: 87.50 } }],
        [{ b: 0, d: 600, x: 410, e: { x: 27 } }],
        [{ b: -1, d: 1, o: -1 }, { b: 0, d: 600, o: 1, e: { o: 5 } }],
        [{ b: -1, d: 1, c: { x: 175.0, t: -175.0 } }, { b: 0, d: 800, c: { x: -175.0, t: 175.0 }, e: { c: { x: 7, t: 7 } } }],
        [{ b: -1, d: 1, o: -1 }, { b: 0, d: 600, x: -570, o: 1, e: { x: 6 } }],
        [{ b: -1, d: 1, o: -1, r: -180 }, { b: 0, d: 800, o: 1, r: 180, e: { r: 7 } }],
        [{ b: 0, d: 1000, y: 80, e: { y: 24 } }, { b: 1000, d: 1100, x: 570, y: 170, o: -1, r: 30, sX: 9, sY: 9, e: { x: 2, y: 6, r: 1, sX: 5, sY: 5 } }],
        [{ b: 2000, d: 600, rY: 30 }],
        [{ b: 0, d: 500, x: -105 }, { b: 500, d: 500, x: 230 }, { b: 1000, d: 500, y: -120 }, { b: 1500, d: 500, x: -70, y: 120 }, { b: 2600, d: 500, y: -80 }, { b: 3100, d: 900, y: 160, e: { y: 24 } }],
        [{ b: 0, d: 1000, o: -0.4, rX: 2, rY: 1 }, { b: 1000, d: 1000, rY: 1 }, { b: 2000, d: 1000, rX: -1 }, { b: 3000, d: 1000, rY: -1 }, { b: 4000, d: 1000, o: 0.4, rX: -1, rY: -1 }]
    ];

    var jssor_1_options = {
        $AutoPlay: 1,
        $SlideDuration: 800,
        $SlideEasing: $Jease$.$OutQuint,
        $CaptionSliderOptions: {
            $Class: $JssorCaptionSlideo$,
            $Transitions: jssor_1_SlideoTransitions
        },
        $ArrowNavigatorOptions: {
            $Class: $JssorArrowNavigator$
        },
        $BulletNavigatorOptions: {
            $Class: $JssorBulletNavigator$
        }
    };

    var jssor_1_slider = new $JssorSlider$("jssor_1", jssor_1_options);

    function ScaleSlider() {
        var refSize = jssor_1_slider.$Elmt.parentNode.clientWidth;
        if (refSize) {
            refSize = Math.min(refSize, 1920);
            jssor_1_slider.$ScaleWidth(refSize);
        } else {
            window.setTimeout(ScaleSlider, 30);
        }
    }
    ScaleSlider();
    $Jssor$.$AddEvent(window, "load", ScaleSlider);
    $Jssor$.$AddEvent(window, "resize", ScaleSlider);
    $Jssor$.$AddEvent(window, "orientationchange", ScaleSlider);
};

jssor_1_slider_init();