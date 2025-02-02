export const UrgencyLevel = {
    ROUTINE: 'routine',
    URGENT: 'urgent',
    EMERGENCY: 'emergency'
};

export const AppointmentType = {
    VIRTUAL: 'virtual',
    IN_PERSON: 'in-person',
    SPECIALIST: 'specialist'
};

export const ModelType = {
    BASIC: 'CHEAP',
    ADVANCED: 'EXPENSIVE'
};

export const ErrorMessages = {
    MAX_NESTED_CALLS: 'Complex medical inquiry detected - please speak with a healthcare provider directly',
    GENERIC_ERROR: 'I apologize, but I encountered an error. Please try rephrasing your question.',
    MEDICAL_ERROR: 'I apologize, but I encountered an error. For medical questions, please consult with a healthcare provider.'
};

export const UI = {
    TITLE: '🏥 AI-Powered Healthcare Triage Assistant',
    DISCLAIMER: `
        ⚕️ Medical Disclaimer: This is a triage assistant only.
        For emergencies, call 911 or your local emergency services immediately.
        This system does not replace professional medical advice.
    `
};