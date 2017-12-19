jQuery(document).ready(function () {
  jQuery('a').on('click', function (e) {
    e.preventDefault();
    jQuery.ajax({
      url: jQuery(this).attr('href'),
      cache: false
    });
  });
});
