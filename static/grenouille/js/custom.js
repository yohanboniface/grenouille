/*
 Custom JS functions
*/

// Toggle categories
jQuery("#panel>h2").click(function () {jQuery("#categories").slideToggle()})
// Toggle area
jQuery("#areas>h2").click(function () {jQuery("#areas>ul").slideToggle()})
// Toggle plus menu
jQuery("#plus_menu>h2").click(function () {jQuery("#plus_menu>ul").slideToggle()})
// Auto scroll to hide the navigation bar in iPhone and iPad (Apple sucks)
var fixSize = function () {
    if ((/(iphone|ipod)/.test(navigator.userAgent.toLowerCase()))) {
        window.scrollTo(0,0);
    }
};

