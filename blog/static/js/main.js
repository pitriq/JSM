(() => {

    document.querySelectorAll('.card').forEach((card) => {
        card.addEventListener('click', (_) => {
            let id = card.getAttribute('data-post-id');
            window.location.href = `/blog/post/${id}`;
        });
    });

})();