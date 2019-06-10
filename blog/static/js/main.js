(() => {

    document.querySelectorAll('.card').forEach((card) => {
        card.addEventListener('click', (_) => {
            let id = card.getAttribute('data-post-id');
            let path = `${window.location.pathname}${window.location.search}`;
            window.location.href = `/blog/post/${id}?from_url=${path}`;
        });
    });

})();