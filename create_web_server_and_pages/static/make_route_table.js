setTimeout(function () {

    // #####################################################################################################
    // ####   ROW   ROW   ROW   ROW   ROW   ROW   ROW   ROW   ROW   ROW   ROW   ROW   ######################
    // #####################################################################################################
    const tables = [document.querySelector("#content-table tbody"), document.querySelector("#container-table")];
    let dragSrcEl = null;
    let dragEnterEl = null;
    let draggedRow = null;
    // document.addEventListener("DOMContentLoaded", () => {

    let placeholder = document.createElement("tr");
    placeholder.className = "placeholder_row";
    placeholder.innerHTML = `<td style="padding: 0px"; colspan="3"></td>`;

    let otherPlaceholder_one = placeholder.cloneNode(true);

    tables.forEach(table => {
        table.addEventListener("dragstart", (e) => {
            if (e.target.tagName !== "TR") return;
            draggedRow = e.target;
            dragSrcEl = null;
            draggedRow.style.opacity = "0.5";
            draggedRow.classList.add("dragging_row");
        });

        table.addEventListener("dragend", (e) => {
            if (e.target.tagName !== "TR") return;
            e.target.style.opacity = "1";
            e.target.classList.remove("dragging_row");
            draggedRow.style.color = null;

            // Add empty row to the Container-Table, if the empty row is pulled away.
            if (draggedRow.closest('table').id == "container-table"
                && placeholder.closest('table').id == "content-table"
                && draggedRow.innerText.trim() == 'XX'
            ) {
                appendNewRow(document.querySelector("#container-table tbody"));
            }
            // Swap the rows if the placeholder is in the DOM
            if (placeholder.parentNode) {
                placeholder.parentNode.insertBefore(draggedRow, placeholder);
                removePlaceholder();
            }
            draggedRow = null;
        });

        table.addEventListener("dragover", (e) => {
            if (!draggedRow) return;
            e.preventDefault();

            var thisTarget = e.target.closest('tbody'); // table.parentNode.id;
            if (thisTarget == null) {
                thisTarget = e.target.closest('table').querySelector('tbody');
            }
            const afterElement = getDragAfterElement(thisTarget, e.clientY);
            if (afterElement == null) {
                thisTarget.appendChild(placeholder);
            } else {
                thisTarget.insertBefore(placeholder, afterElement);
            }
            const x = draggedRow.closest("tbody");

            if (draggedRow.closest("tbody").parentNode == table.parentNode) {
                draggedRow.style.color = null;
            }
            else {
                draggedRow.style.color = "lightgrey";
            }
            // Trigger animation by setting height
            requestAnimationFrame(() => {
                placeholder.style.height = "20px";
            });
        });
    });
    function removePlaceholder() {
        placeholder.style.height = "0"; // Animate back to 0 height
        setTimeout(() => {
            if (placeholder.parentNode) {
                placeholder.remove();
            }
        }, 300); // Wait for the animation to complete before removing
    }

    function getDragAfterElement(container, y) {
        const draggableElements = [...container.querySelectorAll('tr[draggable]:not(.dragging_row)')];

        return draggableElements.reduce((closest, child) => {
            const box = child.getBoundingClientRect();
            const offset = y - box.top - box.height / 2;
            if (offset < 0 && offset > closest.offset) {
                return { offset: offset, element: child };
            } else {
                return closest;
            }
        }, { offset: Number.NEGATIVE_INFINITY }).element;
    }
    // });

    function isRowInCorrectTable(row, targetTable) {
        // Prüfen, ob die Zeile zur ursprünglichen Tabelle gehört
        const sourceTableId = row.closest("tbody").parentElement.id;
        const targetTableId = targetTable.parentElement.id;
        return sourceTableId === targetTableId;
    }
    // #####################################################################################################
    // ####   CELL   CELL   CELL   CELL   CELL   CELL   CELL   CELL   CELL   CELL   CELL   #################
    // #####################################################################################################

    // document.addEventListener('DOMContentLoaded', (event) => {


    function handleDragStart(e) {
        if (e.target.tagName !== "TD") return;
        dragEnterEl = dragSrcEl = this;
        draggedRow = null;
        e.dataTransfer.effectAllowed = 'move';
        e.dataTransfer.setData('text/html', this.innerHTML);
        this.classList.add('dragging'); // Add dragging effect
        // }
    }
    function handleDragOver(e) {
        if (e.target.tagName !== "TD") return;
        if (dragSrcEl === null) return;
        if (e.preventDefault) {
            e.preventDefault();// Allows us to drop
        }
        e.dataTransfer.dropEffect = 'move';
        return false;
    }

    function handleDragEnter(e) {
        if (dragSrcEl === null) return;
        if (e.target.tagName === "TD" && (dragSrcEl === null || dragSrcEl.dataset.column === e.target.dataset.column)) {
            swapContent(true);
            dragEnterEl = this;
            const thisTableCell = this.closest('td');
            if (thisTableCell) {
                thisTableCell.classList.add('over');
                thisTableCell.classList.add('animate');
            }
            swapContent(false);
            dragSrcEl.classList.add('animate');
        } else if (dragSrcEl.tagName === 'TR' && this.closest('table').id === 'content-table') {
            // Dropped placeholder_cell into table          
            const tbody = document.getElementById('content-table');
            const newRow = createNewRow(tbody);
            const rows = [...tbody.rows];
            const dropIndex = rows.indexOf(this.closest('tr'));
            const row = tbody.insertRow(dropIndex);
            row.innerHTML = dragSrcEl.innerHTML;
            row.classList.add('over');
            row.classList.add('animate');
            row.classList.add('placeholder_cell');
        }
    }

    function swapContent(reverse) {
        if (!dragSrcEl || !dragEnterEl) return;
        if (reverse) {
            const savedContent = dragSrcEl.innerHTML;
            dragSrcEl.innerHTML = dragEnterEl.innerHTML;
            dragEnterEl.innerHTML = savedContent;
        } else {
            const savedContent = dragEnterEl.innerHTML;
            dragEnterEl.innerHTML = dragSrcEl.innerHTML;
            dragSrcEl.innerHTML = savedContent;
        }
    }

    function handleDragLeave(e) {
        if (dragSrcEl === null) return;
        if (this.closest('table').id !== 'content-table') return;
        const tbody = document.getElementById('content-table');
        const thisTableCell = this.closest('td');
        if (thisTableCell.classList.contains('placeholder_cell')) {
            const tbody = document.getElementById('content-table');
            const rows = [...tbody.rows];
            const deleteIndex = rows.indexOf(this.closest('tr'));
            tbody.deleteRow(deleteIndex);
        } else if (thisTableCell) {
            thisTableCell.classList.remove('over');
            thisTableCell.classList.remove('animate');
        }
        dragSrcEl.classList.remove('animate');
    }

    function handleDrop(e) {
        if (dragSrcEl === null) return;
        if (e.stopPropagation) {
            e.stopPropagation(); // Stops some browsers from redirecting.
        }
        // firstly: set the old order.        
        swapContent(true);
        if (dragSrcEl.dataset.column === this.dataset.column) {
            // Swap contents within the same column          
            dragSrcEl.innerHTML = this.innerHTML;
            this.innerHTML = e.dataTransfer.getData('text/html');
        }
        return false;
    }

    function handleDragEnd(e) {
        if (dragSrcEl === null) return;
        this.classList.remove('dragging');
        // Remove dragging effect        
        this.classList.remove('over');
        let items = document.querySelectorAll('.draggable');
        items.forEach(function (item) { item.classList.remove('over'); });
    }

    function createNewRow(tbody) {
        const newRow = document.createElement('tr');
        newRow.draggable = true;
        const newCell1 = document.createElement('td');
        newCell1.dataset.column = '1';
        newCell1.className = 'draggable';
        newCell1.draggable = true;
        newCell1.innerHTML = null;

        const newCell2 = document.createElement('td');
        newCell2.dataset.column = '2';
        newCell2.draggable = false;
        newCell2.innerHTML = null;

        const newCell3 = document.createElement('td');
        newCell3.dataset.column = '3';
        newCell3.className = 'draggable';
        newCell3.draggable = true;
        newCell3.innerHTML = null;

        const newCell4 = document.createElement('td');
        newCell4.dataset.column = '4';
        newCell4.draggable = false;
        newCell4.innerHTML = null;
        
        const newCell5 = document.createElement('td');
        newCell5.dataset.column = '5';
        newCell5.className = 'draggable';
        newCell5.draggable = true;
        newCell5.innerHTML = null;

        newRow.appendChild(newCell1);
        newRow.appendChild(newCell2);
        newRow.appendChild(newCell3);
        newRow.appendChild(newCell4);
        newRow.appendChild(newCell5);
        addDragAndDropListeners2Cell(newCell1);
        addDragAndDropListeners2Cell(newCell3);
        addDragAndDropListeners2Cell(newCell5);
        return newRow;
    }

    function addDragAndDropListeners2Cell(element) {
        if (element.tagName !== 'TD') return;
        element.addEventListener('dragstart', handleDragStart, false);
        element.addEventListener('dragenter', handleDragEnter, false);
        element.addEventListener('dragover', handleDragOver, false);
        element.addEventListener('dragleave', handleDragLeave, false);
        element.addEventListener('drop', handleDrop, false);
        element.addEventListener('dragend', handleDragEnd, false);
    }

    // Add event listeners to existing cells      
    let items = document.querySelectorAll('.draggable:not(.placeholder_cell)');
    items.forEach(function (item) { addDragAndDropListeners2Cell(item); });

    document.getElementById("addRow").addEventListener('click',
        () => appendNewRow(document.querySelector("#container-table tbody")));

    document.getElementById("removeRow").addEventListener('click',
        () => removeEmptyRow(document.querySelector("#container-table")));

    function appendNewRow(tbody) {
        const newRow = createNewRow(tbody);
        tbody.append(newRow);

        let items = newRow.querySelectorAll('.draggable:not(.placeholder_cell)');
        items.forEach(function (item) { addDragAndDropListeners2Cell(item); });
    }

    function removeEmptyRow(table) {
        let items = table.querySelectorAll('TR');
        let doDeletion = true;
        items.forEach(function (item) {
            if (doDeletion && item.innerText.trim() == 'XX') {
                var rowIndex = item.rowIndex;
                table.deleteRow(rowIndex);
                doDeletion = false;
            }
        });
    }
    appendNewRow(document.querySelector("#container-table tbody"));

    // ########################################################################################################
    // ########################################################################################################
    // ########################################################################################################
    var allCorrCoeffAsString_skk = document.querySelectorAll("[data-column='2'] span");
    var allCorrCoeffAsString_tt = document.querySelectorAll("[data-column='4'] span");
    var allCorrCoeff_skk = [];
    var allCorrCoeff_tt = [];
    allCorrCoeffAsString_skk.forEach(function (item) {
        var corrCoeff = parseFloat(item.innerText)
        if (!isNaN(corrCoeff)) {
            allCorrCoeff_skk.push(corrCoeff);
            const mTDElement = item.closest('TD');
            if (corrCoeff > 99.0) {
                mTDElement.classList.add('very_good');
            }
            else if (corrCoeff > 80.0) {
                mTDElement.classList.add('good');
            }
            else if (corrCoeff > 70.0) {
                mTDElement.classList.add('normal');
            }
            else if (corrCoeff > 0.0) {
                mTDElement.classList.add('poor');
            }
        }
    });

    allCorrCoeffAsString_tt.forEach(function (item) {
        var corrCoeff = parseFloat(item.innerText)
        if (!isNaN(corrCoeff)) {
            allCorrCoeff_tt.push(corrCoeff);
            const mTDElement = item.closest('TD');
            if (corrCoeff > 99.0) {
                mTDElement.classList.add('very_good');
            }
            else if (corrCoeff > 80.0) {
                mTDElement.classList.add('good');
            }
            else if (corrCoeff > 70.0) {
                mTDElement.classList.add('normal');
            }
            else if (corrCoeff > 0.0) {
                mTDElement.classList.add('poor');
            }
        }
    });
    var trace_ssk = {
        name: 'sbbdb zu sandsteinklettern [' + allCorrCoeff_skk.length + ']',
        x: allCorrCoeff_skk,
        type: 'histogram',
        opacity: 0.5,
        marker: {
            color: 'green',
        }
    };
    var trace_tt = {
        name: 'sbbdb zu teufelsturm [' + allCorrCoeff_tt.length + ']',
        x: allCorrCoeff_tt,
        type: 'histogram',
        opacity: 0.5,
        marker: {
            color: 'blue',
        }
    };
    var layout = {
        bargap: 0.05,
        bargroupgap: 0.2,
        barmode: "overlay",
        height: 250,
        title: "Correlation Distribution",
        xaxis: { title: "Corr.Coeff." },
        yaxis: { title: "Route #Count" },
        showlegend: true,
        legend : {
          title: {
            text: "<b>" 
            + document.querySelector('#filter_summit').options[document.querySelector('#filter_summit').selectedIndex].innerText 
            + ":</b> <br>" 
            + document.querySelectorAll('#content-table > tbody > tr').length + " Wege, Erwähn. & Projekte insgesamt"
          }
        }
    };
    var data = [trace_ssk, trace_tt];
    Plotly.newPlot('myPlotlyDiv', data, layout);

    // });
}, 3000); // How long you want the delay to be, measured in milliseconds.