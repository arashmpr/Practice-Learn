let selectedType = '';
let selectedTitle = '';
let lessons = []; 

function initialPracticeSelection(lessonsData) {
    lessons = lessonsData;
}

function selectPractice(type, title) {
    console.log("in selectPractice");
    openModal(type, title);
}

function openModal(type, title) {
    selectedType = type;
    selectedTitle = title;
    document.getElementById('modalTitle').textContent = title;
    const modal = document.getElementById('lessonModal')
    modal.classList.add('visible', 'opacity-100');
    modal.classList.remove('invisible', 'opacity-0');
            
    const lessonOptionsContainer = document.getElementById('lessonOptions');
    lessonOptionsContainer.innerHTML = '';
            
    lessons.forEach(lesson => {
        const optionDiv = document.createElement('div');
        optionDiv.className = 'lecture-option';
                
        optionDiv.innerHTML = `
        <input type="checkbox" id="lecture-${lesson.id}" class="lecture-checkbox" onchange="updateStartButton()">
        <label for="lecture-${lesson.id}" class="lecture-label">
            <div class="lecture-checkbox-icon"></div>
            <div class="lecture-info">
                <div class="lecture-name">${lesson.name}</div>
                ${lesson.description ? `<div class="lecture-description">${lesson.description}</div>` : ''}
            </div>
        </label>
        `;
                
        lessonOptionsContainer.appendChild(optionDiv);
    });
            
    document.getElementById('lessonModal').classList.add('active');
    document.body.style.overflow = 'hidden';
}

function closeModal() {
    const modal = document.getElementById('lessonModal')
    modal.classList.remove('active');
    modal.classList.add('invisible', 'opacity-0');
    modal.classList.remove('visible', 'opacity-100');
    document.body.style.overflow = '';

    setTimeout(() => {
        document.getElementById('selectAll').checked = false;
        document.querySelectorAll('.lecture-checkbox').forEach(cb => cb.checked = false);
        updateStartButton();
    }, 300);
}

function toggleSelectAll() {
    const selectAllCheckbox = document.getElementById('selectAll');
    const lectureCheckboxes = document.querySelectorAll('.lecture-checkbox');
        
    lectureCheckboxes.forEach(checkbox => {
        checkbox.checked = selectAllCheckbox.checked;
    });
        
    updateStartButton();
}

function updateStartButton() {
    const checkedLessons = document.querySelectorAll('.lecture-checkbox:checked');
    const startBtn = document.getElementById('startPracticeBtn');
    startBtn.textContent = `Start Practice`;
        
    if (checkedLessons.length > 0) {
        startBtn.disabled = false;
    } else {
        startBtn.disabled = true;
    }
        
    const selectAllCheckbox = document.getElementById('selectAll');
    const totalLectures = document.querySelectorAll('.lecture-checkbox').length;
        
    if (checkedLessons.length === 0) {
        selectAllCheckbox.indeterminate = false;
        selectAllCheckbox.checked = false;
    } else if (checkedLessons.length === totalLectures) {
        selectAllCheckbox.indeterminate = false;
        selectAllCheckbox.checked = true;
    } else {
        selectAllCheckbox.indeterminate = true;
    }
}

function startPractice() {
    console.log("Starting practice...");
    
    const selectedLessons = Array.from(document.querySelectorAll('.lecture-checkbox:checked'))
        .map(cb => cb.id.replace('lecture-', ''));
    const numQuestions = document.getElementById('modalNumQuestions').value;
        
    if (selectedLessons.length === 0) {
        alert('Please select at least one lecture.');
        return;
    }
        
    // Build URL with selected lectures
    const lessonParams = selectedLessons.map(id => `lessons=${id}`).join('&');
    const url = `/start/?practice_type=${selectedType}&num_questions=${numQuestions}&${lessonParams}`;
        
    console.log('Starting practice with URL:', url);
    console.log('Selected practice type:', selectedType);
    console.log('Selected lessons:', selectedLessons);
    
    window.location.href = url;
    closeModal();
}

// Initialize event listeners when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    const modal = document.getElementById("lectureModal");
    if (modal) {
        modal.addEventListener('click', function(e) {
            if (e.target == this) {
                closeModal();
            }
        });
    }
    document.addEventListener('keydown', function(e) {
        if (e.key == 'Escape' && document.getElementById("lectureModal").classList.contains('active')) {
            closeModal();
        }
    });
});