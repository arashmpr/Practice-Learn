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

  const modal = document.getElementById('lessonModal');
  const modalContent = modal.querySelector('.modal-content');
  const lessonOptionsContainer = document.getElementById('lessonOptions');

  // Set modal title
  document.getElementById('modalTitle').textContent = title;

  // Show modal background
  modal.classList.remove('invisible', 'opacity-0');
  modal.classList.add('visible', 'opacity-100');

  // Animate modal content
  modalContent.classList.remove('opacity-0', 'scale-95', 'translate-y-6');
  modalContent.classList.add('opacity-100', 'scale-100', 'translate-y-0');

  // Prevent background scroll
  document.body.style.overflow = 'hidden';

  // Clear previous lessons
  lessonOptionsContainer.innerHTML = '';

  // Populate lessons
  lessons.forEach(lesson => {
    const optionDiv = document.createElement('div');
    optionDiv.className = 'lecture-option flex items-start gap-3 p-3 rounded-lg border border-gray-200 hover:border-sky-400 transition';

    optionDiv.innerHTML = `
      <input type="checkbox" id="lecture-${lesson.id}" class="lecture-checkbox mt-1 text-sky-600 focus:ring-sky-500 rounded" onchange="updateStartButton()">
      <label for="lecture-${lesson.id}" class="flex flex-col text-sm text-gray-800 cursor-pointer w-full">
        <span class="font-medium">${lesson.name}</span>
        ${lesson.description ? `<span class="text-gray-500 text-xs mt-1">${lesson.description}</span>` : ''}
      </label>
    `;

    lessonOptionsContainer.appendChild(optionDiv);
  });
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