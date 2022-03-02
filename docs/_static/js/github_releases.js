window.onload = () => {
    const table = document.getElementById("downloadTable");
    if (!table) return;
    fetch("https://api.github.com/repos/ShinoYasx/tat/releases/latest", {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/vnd.github.v3+json'
        }
    })
        .then((res) => res.json())
        .then((data) => {
            let totalCount = 0;
            data.assets.forEach(asset => {
                const row = table.insertRow();
                const assetName = row.insertCell();
                const downloadCount = row.insertCell();

                assetName.innerHTML = '<a href=' + asset.browser_download_url + '>' + asset.name + '</a>';
                downloadCount.innerHTML = asset.download_count;
                totalCount += asset.download_count;
            })
            const row = table.insertRow();
            const totalTitle = row.insertCell();
            const total = row.insertCell();
            total.innerHTML = totalCount;
            totalTitle.innerHTML = '<b>Total</b>'
        })
}