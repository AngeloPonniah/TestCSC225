document.getElementById('LoadFacts').addEventListener('click', function() {
    fetch('https://brianobruno.github.io/cats.json')
    .then(response => response.json())
    .then(data => {
        data.facts.sort((a, b) => a.factID - b.factID);
        const table = document.getElementById('factsTable');
        table.innerHTML = '<tr><th>Fact ID </th><th>Fact</th></tr>';
        data.facts.forEach(fact => {
            const row = table.insertRow(-1);
            const cell1 = row.insertCell(0);
            const cell2 = row.insertCell(1);
            cell1.innerHTML = fact.factID;
            cell2.innerHTML = fact.text;
        });

        // Update image
        const imgElement = document.getElementById('catPhoto');
        imgElement.src = data.catPhoto;
        console.log(data.catPhoto);
    })
    .catch(error => console.error('Error fetching data:', error));
});
