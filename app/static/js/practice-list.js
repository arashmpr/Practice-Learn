// Global variables to store current quiz selection
let selectedQuizType = '';
let selectedQuizName = '';
let lessons = []; // This will be populated from the template

function initializeQuizSelection(lessonsData) {
    lessons = lessonsData;
}

function selectQuiz(quizType, quizName) {
    openLectureModal(quizType, quizName);
}

function openLectureModal(quizType, quizName) {
    selectedQuizType = quizType;
    selectedQuizName = quizName;
    document.getElementById('modalTitle').textContent = quizName;
            
    const lectureOptionsContainer = document.getElementById('lectureOptions');
    lectureOptionsContainer.innerHTML = '';
            
    lectures.forEach(lecture => {
        const optionDiv = document.createElement('div');
        optionDiv.className = 'lecture-option';
                
        optionDiv.innerHTML = `
        <input type="checkbox" id="lecture-${lecture.id}" class="lecture-checkbox" onchange="updateStartButton()">
        <label for="lecture-${lecture.id}" class="lecture-label">
            <div class="lecture-checkbox-icon"></div>
            <div class="lecture-info">
                <div class="lecture-name">${lecture.name}</div>
                ${lecture.description ? `<div class="lecture-description">${lecture.description}</div>` : ''}
            </div>
        </label>
        `;
                
        lectureOptionsContainer.appendChild(optionDiv);
    });
            
    document.getElementById('lectureModal').classList.add('active');
    document.body.style.overflow = 'hidden';
}

function closeLectureModal() {
    document.getElementById('lectureModal').classList.remove('active');
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
    const checkedLectures = document.querySelectorAll('.lecture-checkbox:checked');
    const startBtn = document.getElementById('startQuizBtn');
    startBtn.textContent = `Start Quiz`;
        
    if (checkedLectures.length > 0) {
        startBtn.disabled = false;
    } else {
        startBtn.disabled = true;
    }
        
    const selectAllCheckbox = document.getElementById('selectAll');
    const totalLectures = document.querySelectorAll('.lecture-checkbox').length;
        
    if (checkedLectures.length === 0) {
        selectAllCheckbox.indeterminate = false;
        selectAllCheckbox.checked = false;
    } else if (checkedLectures.length === totalLectures) {
        selectAllCheckbox.indeterminate = false;
        selectAllCheckbox.checked = true;
    } else {
        selectAllCheckbox.indeterminate = true;
    }
}

function startQuizWithLectures() {
    console.log("Starting quiz with lectures...");
    
    const selectedLectures = Array.from(document.querySelectorAll('.lecture-checkbox:checked'))
        .map(cb => cb.id.replace('lecture-', ''));
    const numQuestions = document.getElementById('modalNumQuestions').value;
        
    if (selectedLectures.length === 0) {
        alert('Please select at least one lecture.');
        return;
    }
        
    // Build URL with selected lectures
    const lectureParams = selectedLectures.map(id => `lectures=${id}`).join('&');
    const url = `/start/?quiz_type=${selectedQuizType}&num_questions=${numQuestions}&${lectureParams}`;
        
    console.log('Starting quiz with URL:', url);
    console.log('Selected quiz type:', selectedQuizType);
    console.log('Selected lectures:', selectedLectures);
    
    window.location.href = url;
    closeLectureModal();
}

// Initialize event listeners when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    // Close modal when clicking outside
    const modal = document.getElementById("lectureModal");
    if (modal) {
        modal.addEventListener('click', function(e) {
            if (e.target == this) {
                closeLectureModal();
            }
        });
    }

    // Close modal with Escape key
    document.addEventListener('keydown', function(e) {
        if (e.key == 'Escape' && document.getElementById("lectureModal").classList.contains('active')) {
            closeLectureModal();
        }
    });
});