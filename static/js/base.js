$(document).ready(function () {
    $('.like_button').click(function (event) {

        // Get required data
        let target = $(event.currentTarget);
        let article_id = target.data('id');
        let article_action = target.data('action');
        let article_like_url = target.data('like_url');

        // Get icon and count elements
        let like_icon = target.find('.like_icon');
        let like_count = target.find('.like_count');

        // Make ajax request to article url sending article id and action
        $.ajax({
            url: article_like_url,
            data: {
                article_id: article_id,
                article_action: article_action,
            },
        }).done(function (data) {
            // When complete, check to see if was successful
            if (data.success) {
                // If we liked, update elements to match.
                if (article_action === 'like') {
                    target.removeClass('btn-outline-primary');
                    target.addClass('btn-primary');
                    like_icon.removeClass('bi-hand-thumbs-up');
                    like_icon.addClass('bi-hand-thumbs-up-fill');
                    like_count.html(Number(like_count.html()) + 1);
                    // Else, update elements to match unlike.
                } else {
                    target.removeClass('btn-primary');
                    target.addClass('btn-outline-primary');
                    like_icon.removeClass('bi-hand-thumbs-up-fill');
                    like_icon.addClass('bi-hand-thumbs-up');
                    like_count.html(Number(like_count.html()) - 1);
                }
            }
        });
    });
});
