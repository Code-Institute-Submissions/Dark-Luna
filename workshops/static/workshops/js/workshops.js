/*jshint esversion: 6 */
/**
 * This function will reload Lessons page and display/filter lessons with selected Sort Option only
 */
 $('.sort-selector').change(function () {
    let selector = $(this);
    let currentUrl = new URL(window.location);
    let selectedVal = selector.val();
    if (selectedVal != "reset") {
        let sort = selectedVal.split("_")[0];
        let direction = selectedVal.split("_")[1];
        currentUrl.searchParams.set("sort", sort);
        currentUrl.searchParams.set("direction", direction);
        window.location.replace(currentUrl);
    } else {
        currentUrl.searchParams.delete("sort");
        currentUrl.searchParams.delete("direction");
        window.location.replace(currentUrl);
    }
});

/**
 * This function will add special id to anchor element to set 'category-selected' style
 */
$(function () {
    let pathname = window.location.href;
    let category_in = pathname.search("category");
    // check if path name contains
    if (pathname.search("=") < 0) { } else {
        pathname = pathname.split('=')[1];
        let last_sign = pathname.search("&");

        if (last_sign <= 0) {
            // add categroy.name-selected class to element when window href doesn't contains category or filtering
            category_selected = pathname + '-selected';
            $('.pathname').html(pathname);
            let my_id = '.' + pathname;
            $(my_id).addClass('category-selected');
        } else {
            // add category.name-selected class to element when category is filtered
            category_selected = pathname.substring(0, last_sign); + '-selected';
            $('.pathname').html(category_selected);
            let my_id = '.' + category_selected;
            if (category_in == -1) {
                $('.all-lessons').addClass('category-selected');
            } else {
                $(my_id).addClass('category-selected');
            }
        }
    }
});