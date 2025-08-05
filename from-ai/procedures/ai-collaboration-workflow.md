# AI Collaboration Workflow

## Pre-Session Preparation

### For Daniel
1. Update `for-ai/prompts/iteration-template.md` with current session goals
2. Add any new context files to `for-ai/context/`
3. Include error logs or debugging info in `for-ai/debugging/`
4. Review previous session log in `from-ai/session-logs/`

### For AI Agent
1. Read the latest iteration prompt
2. Review all context files
3. Check previous session logs for continuity
4. Understand current project state

## During Development Session

### AI Agent Responsibilities
- Follow the specific requests in the iteration prompt
- Document decisions and reasoning
- Ask clarifying questions when requirements are unclear
- Provide progress updates during long tasks

### Daniel's Responsibilities
- Provide clear, specific instructions
- Test and validate AI-generated code
- Provide feedback on solutions
- Update context files as needed

## Post-Session Tasks

### AI Agent Must Complete
1. Create session log in `from-ai/session-logs/session-YYYY-MM-DD.md`
2. Update documentation in `from-ai/documentation/` if architecture changed
3. Note any procedures that should be documented in `from-ai/procedures/`

### Daniel Should Review
1. Session log for accuracy
2. Code changes for quality and correctness
3. Documentation updates for completeness
4. Next session priorities

## File Organization Best Practices

### for-ai/ Folder
- Keep prompts specific and actionable
- Update context files regularly
- Archive old debugging logs when resolved
- Use descriptive filenames with dates

### from-ai/ Folder
- Session logs should be comprehensive but concise
- Documentation should be maintainable by Daniel
- Procedures should be step-by-step and clear
- Use consistent formatting across all files

## Quality Standards

### Code Quality
- Follow project coding standards
- Include appropriate comments
- Write testable code
- Consider maintainability

### Documentation Quality
- Use clear, concise language
- Include examples where helpful
- Keep information current
- Structure for easy navigation

---
*This workflow should be updated as we learn what works best for our collaboration.*
