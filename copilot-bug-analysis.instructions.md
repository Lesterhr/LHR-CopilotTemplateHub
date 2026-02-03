# Bug Analysis Agent Protocol

**Version**: 1.0  
**Last Updated**: February 2026  
**Purpose**: Guide AI agents in exhaustive reactive bug analysis to identify ALL root causes

---

## Purpose and Scope

**Purpose**: Perform exhaustive reactive bug analysis to identify ALL root causes of reported issues and produce actionable documentation for human developers.

**Scope**: Reactive analysis only - analyze bugs after they are reported by users or QA.

**Critical Constraint**: This is a **READ-ONLY** analysis protocol. **DO NOT make any code changes**. Your only goal is to identify and document all reasons causing the bug for human developers to implement.

**Output Audience**: Human developers who will apply the fixes. Provide clear, actionable documentation with exact locations and implementation steps.

**Output Format**: Analysis results must be provided as Markdown (.md) format with diff-style code blocks.

**Language Applicability**: This protocol applies to codebases in any programming language.

---

## When to Use This Protocol

This protocol activates when you receive:
- A bug report from a user, QA tester, or issue tracker
- A request to analyze unexpected behavior
- An investigation task for production failures

**Invocation**: Load these instructions when beginning bug analysis. Follow all phases in sequence before declaring analysis complete.

---

## Case Study: The Multi-Cause Bug Pattern

### Why This Protocol Exists

Bug analysis often fails because developers and AI agents stop after finding the first issue. This case study demonstrates why exhaustive analysis is critical.

### Scenario: The Batch Operation Failure

**User Report**:
> "The batch processing mode fails with an error, but when I process items individually, everything works fine. Both modes should do the same thing."

**Initial Analysis** (❌ Incomplete):

Agent found this code in a helper method:

```csharp
// Helper method called by batch processor
public void UpdateHelper(Item item, Connection connection)
{
    if (item.Mode == ProcessingMode.Shared)
    {
        // Update records in database
        string sqlUpdate = $"UPDATE {connection.Schema}.ITEMS WHERE ID='{item.Id}' AND PROJECT!='{connection.ProjectId}'";
        connection.Database.Execute(sqlUpdate);
    }
}
```

**Issue #1 Found**: SQL UPDATE statement is malformed - missing the `SET` clause.

**Fix Applied**:
```diff
- string sqlUpdate = $"UPDATE {connection.Schema}.ITEMS WHERE ID='{item.Id}' AND PROJECT!='{connection.ProjectId}'";
+ string sqlUpdate = $"UPDATE {connection.Schema}.ITEMS SET STATUS='valid' WHERE ID='{item.Id}' AND PROJECT!='{connection.ProjectId}'";
```

**Developer applied this fix, but bug persisted!**

---

### Deeper Analysis Revealed Second Issue

The agent went back and compared the working vs broken code paths:

```csharp
// Method A: Single item processing (✅ WORKS)
public void ProcessSingle(Item item, Connection connection)
{
    // Handles invalid items inline
    if (item.IsInvalid)
    {
        // Sets required properties
        item.Status = "processed";
        item.Timestamp = DateTime.Now;
        item.ProcessedBy = connection.CurrentUser;
        
        // Updates database
        connection.Database.Update(item);
    }
    
    // Continues with normal processing
    NormalProcessing(item);
}

// Method B: Batch processing (❌ FAILS)
public void ProcessBatch(List<Item> items, Connection connection)
{
    // Handles invalid items via helper
    foreach (var item in items)
    {
        if (item.IsInvalid)
        {
            UpdateHelper(item, connection);  // ← Calls helper with SQL bug
        }
    }
    
    // ❌ MISSING: Property initialization that ProcessSingle does
    // ❌ MISSING: item.Status = "processed"
    // ❌ MISSING: item.Timestamp = DateTime.Now
    // ❌ MISSING: item.ProcessedBy = connection.CurrentUser
    
    // Continues with normal processing
    foreach (var item in items)
    {
        NormalProcessing(item);
    }
}
```

**Issue #2 Found**: `ProcessBatch` doesn't set required properties (`Status`, `Timestamp`, `ProcessedBy`) that `ProcessSingle` sets before database operations.

---

### The Complete Fix Required

**Both issues needed fixing**:

1. **Fix SQL syntax in `UpdateHelper`** (line 8):
```diff
public void UpdateHelper(Item item, Connection connection)
{
    if (item.Mode == ProcessingMode.Shared)
    {
-       string sqlUpdate = $"UPDATE {connection.Schema}.ITEMS WHERE ID='{item.Id}' AND PROJECT!='{connection.ProjectId}'";
+       string sqlUpdate = $"UPDATE {connection.Schema}.ITEMS SET STATUS='valid' WHERE ID='{item.Id}' AND PROJECT!='{connection.ProjectId}'";
        connection.Database.Execute(sqlUpdate);
    }
}
```

2. **Add missing property initialization in `ProcessBatch`** (line 18):
```diff
public void ProcessBatch(List<Item> items, Connection connection)
{
    foreach (var item in items)
    {
        if (item.IsInvalid)
        {
+           // Initialize required properties (like ProcessSingle does)
+           item.Status = "processed";
+           item.Timestamp = DateTime.Now;
+           item.ProcessedBy = connection.CurrentUser;
+           
            UpdateHelper(item, connection);
        }
    }
    
    foreach (var item in items)
    {
        NormalProcessing(item);
    }
}
```

---

### The Lesson

When code paths diverge (Method A works, Method B fails, both do "the same thing"):

✅ Check syntax/API calls in ALL methods and their helpers  
✅ Compare implementations line-by-line to find missing logic blocks  
✅ Verify property initialization is complete in all paths  
✅ Test that EACH fix is necessary (removing any fix re-breaks the system)  

**Stopping at the first issue leaves the bug only partially fixed.**

This is why the protocol requires checking ALL code paths, helper methods, and similar implementations before declaring analysis complete.

---

## Bug Analysis Protocol

Follow these phases in order. Complete each checkpoint before proceeding to the next.

---

### Phase 1: Symptom Identification

- [ ] **Parse the bug report**: Extract concrete symptoms (error messages, unexpected behavior, conditions)
- [ ] **Identify affected scenarios**: What works? What fails? Under what conditions?
- [ ] **Document expected behavior**: What should happen instead?

**Output**: Clear description of symptom and failure conditions.

---

### Phase 2: Code Path Mapping

- [ ] **Trace execution paths**: Map ALL code paths that could produce the reported symptom
- [ ] **Include entry points**: UI events, API endpoints, CLI commands, scheduled jobs
- [ ] **Follow the chain**: Method calls → Helper methods → Database/API operations
- [ ] **Note conditional branches**: Different behavior based on flags, modes, or data states

**Output**: List of all code paths from entry point to symptom occurrence.

**Example**:
```
Path 1: UserInterface.ProcessButton → ProcessSingle() → NormalProcessing() ✅ Works
Path 2: UserInterface.ProcessAllButton → ProcessBatch() → UpdateHelper() → NormalProcessing() ❌ Fails
Path 3: CLI.RunBatch → ProcessBatch() → UpdateHelper() → NormalProcessing() ❌ Fails
```

---

### Phase 3: Reference Implementation Discovery

- [ ] **Find working similar code**: Locate methods that do similar operations successfully
- [ ] **Identify method families**: Methods with similar names (Process vs ProcessBatch vs ProcessTotal)
- [ ] **Check version history**: Previous working versions, parallel implementations
- [ ] **Look for patterns**: Repeated logic that might have inconsistencies

**Output**: One or more reference implementations that work correctly.

**Example**:
```
Reference: ProcessSingle() successfully handles invalid items
Broken: ProcessBatch() fails with same items
Both should: Set properties, update database, continue processing
```

---

### Phase 4: Systematic Comparison

- [ ] **Line-by-line comparison**: Compare broken code path against working reference
- [ ] **Catalog ALL differences**: Missing code blocks, different method calls, property assignments
- [ ] **Check helper methods**: If broken path calls helpers, analyze helper implementations thoroughly
- [ ] **Validate operations**: Check syntax of SQL, API calls, file operations, string formatting

**Key Patterns to Check**:

#### 1. Syntax/Format Errors
- SQL statements: `UPDATE` without `SET`, `INSERT` without `VALUES`, `DELETE` without `WHERE`
- API calls: Missing required parameters, wrong method signatures, incorrect argument order
- String formatting: Unclosed braces, wrong placeholders, escaping issues
- File paths: Incorrect separators, missing extensions, wrong casing on case-sensitive systems

#### 2. Missing Logic Blocks
- Code present in Method A but completely absent in Method B
- Property assignments in one path but not another
- Validation checks in working code, missing in broken code
- Exception handling present in one variant, missing in another

#### 3. Incomplete Initialization
- Properties set before operations in working code
- Missing timestamp/audit fields
- Null values where working code provides defaults
- Configuration values loaded in one path but not another

#### 4. Wrong Conditional Logic
- Different values in if/else branches
- Missing cases in switch statements
- Inverted boolean conditions
- Off-by-one errors in loop boundaries

**Output**: Detailed list of every divergence between working and broken code.

---

### Phase 5: Issue Classification

For each divergence found, classify:

- [ ] **Syntax Error**: Malformed statements that cause runtime/compilation errors
- [ ] **Logic Gap**: Missing code blocks that cause incorrect behavior
- [ ] **Data Issue**: Missing initialization, null values, wrong defaults
- [ ] **Intentional Design**: Legitimate difference (not a bug - document why)

**Output**: Categorized list of issues vs intentional differences.

---

### Phase 6: Root Cause Validation

For each identified issue, verify:

- [ ] **Can this cause the symptom?** Trace how this issue leads to reported behavior
- [ ] **Is this issue necessary to fix?** Would fixing only others leave this causing problems?
- [ ] **Are there related issues?** Does this issue suggest similar problems elsewhere?
- [ ] **Can I prove it?** Can I explain the causal chain from issue to symptom?

**Critical**: Do not stop after finding one issue. Check if multiple issues compound to create the bug.

---

### Phase 7: Completeness Check

Before proceeding to documentation phase, verify:

- [ ] **All code paths analyzed**: Have you checked every path that could produce the symptom?
- [ ] **All helper methods checked**: Have you analyzed methods called by broken paths?
- [ ] **All similar methods compared**: Have you checked parallel implementations?
- [ ] **All conditional branches validated**: Have you checked both if/else, all switch cases?
- [ ] **Each fix independently justified**: Can you explain why EACH issue must be fixed?
- [ ] **Removal test**: Would removing any single fix cause the bug to persist?

**If you answer "no" or "uncertain" to any question, return to previous phases.**

---

### Phase 8: Developer Documentation Generation

**This is the final mandatory step. Generate actionable documentation for human developers.**

Your output must include:

1. **Exact Locations**: File paths with line numbers for each issue
2. **Diff-Style Code Blocks**: Before/after for every fix using unified diff format
3. **Numbered Steps**: Sequential implementation instructions
4. **Testing Steps**: How to verify each fix works
5. **Combined Validation**: Why all fixes together solve the bug

**Requirements**:
- Use clear section headings
- Apply syntax highlighting to code blocks
- Number implementation steps sequentially
- Show context lines around changes in diffs
- Explain dependencies between fixes

**Proceed to Output Format section for complete template.**

---

## Required Output Format

Your analysis must be provided as a Markdown (.md) document with the following structure:

```markdown
# Bug Analysis Report: [Brief Title]

**Analyzed By**: AI Bug Analysis Agent  
**Date**: [Date]  
**Protocol Version**: [Version]  
**Bug Report**: [Reference to original report]

---

## Executive Summary

**Symptom**: [One-sentence description of failure]  
**Root Causes Found**: [N] distinct issues identified  
**Affected Code Paths**: [List entry points]  
**Fix Complexity**: [Simple/Moderate/Complex]

---

## Symptom Analysis

### What Fails
[Specific failure behavior with error messages if available]

### What Works
[Similar functionality that succeeds]

### Failure Conditions
[When/how does failure occur - steps to reproduce]

---

## Code Paths Analyzed

### Path 1: [Name] ✅ Works / ❌ Fails
**Entry Point**: [File:Line]  
**Flow**: [Method1 → Method2 → Method3]  
**Outcome**: [Success/Failure description]

### Path 2: [Name] ✅ Works / ❌ Fails
**Entry Point**: [File:Line]  
**Flow**: [Method1 → Method2 → Method3]  
**Outcome**: [Success/Failure description]

[Repeat for all paths]

---

## Reference Implementation

**Working Code**: [File:Line - Method name]  
**Why It Works**: [Brief explanation of correct behavior]  
**Used As Baseline**: For comparison with broken implementations

---

## Root Causes Identified

### Issue #1: [Category] - [Brief Description]

**Severity**: High/Medium/Low  
**Location**: `[File:Line]` - `[MethodName]`  
**Type**: Syntax Error / Logic Gap / Data Issue

**Description**:  
[Detailed explanation of what is wrong]

**Current Code** (Broken):
```[language]
[Code snippet with issue - include context lines]
```

**Fixed Code** (Required):
```[language]
[Code snippet with fix applied]
```

**Diff**:
```diff
  [context line before]
  [context line before]
- [old line to remove]
+ [new line to add]
  [context line after]
  [context line after]
```

**Impact**:  
[How this specific issue contributes to the bug - be explicit]

**Why This Fix Is Necessary**:  
[What would still fail if only this were fixed, or why this fix enables others]

---

### Issue #2: [Category] - [Brief Description]

[Same structure as Issue #1]

---

[Repeat for all issues]

---

## Implementation Guide

### Prerequisites
- [ ] [Any setup needed before applying fixes]
- [ ] [Backup considerations]
- [ ] [Build environment ready]

### Step-by-Step Implementation

#### Step 1: Fix [Issue #1 Description]
**File**: `[Path/To/File.ext]`  
**Line**: [Line number]  
**Action**: [What to change]

```diff
[Diff showing the change]
```

**Validation**: [How to verify this specific fix]

---

#### Step 2: Fix [Issue #2 Description]
**File**: `[Path/To/File.ext]`  
**Line**: [Line number]  
**Action**: [What to change]

```diff
[Diff showing the change]
```

**Validation**: [How to verify this specific fix]

---

[Repeat for all fixes]

---

### Testing & Verification

#### Test Case 1: [Scenario]
**Steps**:
1. [Step to reproduce original bug]
2. [Step to reproduce original bug]
3. [Expected to fail before fix]

**Expected After Fix**: [Correct behavior]

#### Test Case 2: [Scenario]
[Same structure]

#### Regression Testing
- [ ] Verify working code paths still work (Path 1, etc.)
- [ ] Test both success and failure conditions
- [ ] Check edge cases: [list specific edge cases]

---

## Why All Fixes Are Necessary

### If Only Issue #1 Fixed:
[Explain what would still fail and why]

### If Only Issue #2 Fixed:
[Explain what would still fail and why]

### Combined Effect:
[Explain why all fixes together solve the complete bug]

**Dependencies Between Fixes**: [Explain if fixes must be applied in specific order]

---

## Other Code Paths Verified

The following similar code was checked and confirmed NOT to have these issues:

- ✅ `[File:Line]` - `[MethodName]` - [Why it's correct]
- ✅ `[File:Line]` - `[MethodName]` - [Why it's correct]

---

## Analysis Completeness Checklist

- [x] All code paths producing symptom analyzed
- [x] All helper methods checked for issues
- [x] All similar method variants compared
- [x] Each issue independently validated with causal chain
- [x] Confirmed no single fix resolves bug alone - all required
- [x] Diff-style code blocks provided for each fix
- [x] Step-by-step implementation guide created
- [x] Testing verification steps documented
- [x] Regression testing considerations noted

---

## Additional Notes

[Any other relevant information, assumptions, or concerns for the developer]

---

*Analysis completed following Bug Analysis Agent Protocol v[Version]*
```

---

## Analysis Principles

### 1. Exhaustive Over Expedient
Better to over-analyze than to miss issues. When in doubt, check it. False positives can be filtered by developers; false negatives leave bugs unfixed.

### 2. Compare Don't Assume
Always find working reference code. Don't assume how things "should" work based on documentation or naming. Compare actual implementations.

### 3. Validate Each Fix
Explain why EACH identified issue is necessary to fix. Prove none are red herrings. Show the causal chain from issue to symptom.

### 4. Think in Patterns
One missing property suggests checking all properties in that method. One helper bug suggests checking all helpers called by that code path. Bugs cluster.

### 5. Developer-Centric Output
Format for the human who will implement fixes. Exact locations, clear diffs, numbered steps. Make it easy to apply fixes correctly.

### 6. No Code Changes
Your role is analysis and documentation only. Do not implement fixes. Do not modify files. Provide complete documentation for developers to act on.

---

## Common Pitfalls to Avoid

### ❌ Stopping at First Issue
**Don't**: "Found malformed SQL, analysis complete"  
**Do**: Continue checking for missing logic, incomplete initialization, wrong conditionals

### ❌ Assuming Similar Code is Similar
**Don't**: "Method A and Method B have same name, must work same way"  
**Do**: Compare implementations line-by-line regardless of naming

### ❌ Ignoring Helper Methods
**Don't**: "The main method looks fine"  
**Do**: Analyze every method the broken path calls, including helpers and utilities

### ❌ Skipping Conditional Branches
**Don't**: "Checked the if block, looks good"  
**Do**: Check both if/else, all switch cases, all loop variants

### ❌ Accepting Partial Fixes
**Don't**: "This should probably fix it"  
**Do**: Validate completeness - explain why partial fix would fail

### ❌ Vague Locations
**Don't**: "There's an issue in the ProcessBatch method"  
**Do**: "Line 47 in `src/Services/BatchProcessor.cs` - missing property initialization"

### ❌ Missing Diff Context
**Don't**: Show only the changed line  
**Do**: Include 2-3 context lines before and after for clarity

---

## Living Document: Lessons Learned Repository

**This protocol evolves through real-world usage.**

After developers apply fixes and provide feedback about:
- What worked well in the analysis
- What was missing or unclear
- New bug patterns discovered
- Techniques that proved effective

**This section will be updated when explicitly requested by the maintainer.**

**Do not auto-update this document.** Lessons are added manually when the maintainer provides feedback after bug resolution.

---

### How to Add Lessons Learned

When requested to add a lesson, use this format:

```markdown
### [Tool Name] - [Pattern Type] - [Language] (Added: v[Version], [Date])

**Bug ID**: [Reference]  
**Symptom Pattern**: [Brief description]  
**Root Cause Category**: Syntax Error / Logic Gap / Data Issue / [Other]  
**What Made It Hard to Find**: [Why initial analysis might miss this]  
**Analysis Technique That Worked**: [How to reliably find this pattern]  
**Code Pattern to Watch For**: [Specific code smell or pattern]  

**Example Code Pattern**:
```[language]
[Minimal example showing the pattern]
```

**Detection Checklist**:
- [ ] [Specific thing to check]
- [ ] [Specific thing to check]
```

---

### Lesson Organization Structure

Lessons are organized by: **Tool → Pattern Type → Language**

```
├── [Tool Name 1]
│   ├── Syntax Errors
│   │   ├── C#
│   │   ├── Python
│   │   └── JavaScript
│   ├── Logic Gaps
│   │   ├── C#
│   │   └── Python
│   └── Data Issues
│       └── C#
├── [Tool Name 2]
│   └── ...
└── Generic (Cross-Tool Patterns)
    └── ...
```

---

### Lessons Learned Entries

*No lessons recorded yet. This section will grow as bugs are analyzed and resolved.*

---

#### Example Template (Remove when first real lesson is added):

```markdown
### Example Tool - Syntax Errors - C# (Added: v1.1, 2026-02-15)

**Bug ID**: #1234  
**Symptom Pattern**: Batch operations fail with database errors while single operations succeed  
**Root Cause Category**: Syntax Error  
**What Made It Hard to Find**: Error occurred in helper method only called by batch path, not main method  
**Analysis Technique That Worked**: Compared working single vs broken batch, then analyzed all helpers called by batch path  
**Code Pattern to Watch For**: SQL UPDATE/INSERT statements in helper methods with inconsistent formatting  

**Example Code Pattern**:
```csharp
// Helper methods with SQL operations - check syntax carefully
public void UpdateHelper(Item item)
{
    // ❌ Easy to miss: UPDATE missing SET clause
    string sql = $"UPDATE Items WHERE Id='{item.Id}'";
}
```

**Detection Checklist**:
- [ ] Check ALL SQL statements in helper methods for complete syntax
- [ ] Verify UPDATE has SET, INSERT has VALUES, DELETE has WHERE (unless intentional)
- [ ] Compare SQL in helpers against SQL in main methods
```

---

## Framework-Agnostic Invocation

This protocol can be loaded by:

- **GitHub Copilot**: `@workspace Analyze this bug following bug-analysis protocol in .github/copilot-instructions-bug-analysis.md`
- **Custom agents**: Load this file as system prompt before analysis
- **Manual analysis**: Use as checklist when investigating bugs
- **Code review**: Apply protocol when reviewing bug fixes for completeness

**Key Requirements**:
- Agent must have read access to full codebase
- Agent must follow ALL protocol phases before outputting analysis
- Agent must use the complete output format template
- Agent must not modify code files

---

## Protocol Versioning

### Version History

**v1.0** (February 2026)
- Initial protocol release
- 8-phase analysis workflow
- Multi-cause bug case study
- Developer-centric output format
- Lessons learned repository structure

### Version Increment Policy

**Minor Version (v1.x)**: 
- New lesson learned added
- New detection pattern added
- Clarification to existing phase
- Enhanced output template section

**Major Version (v2.0)**:
- Core protocol structure changed
- Phases added/removed/reordered
- Fundamental methodology shift
- Breaking changes to output format

---

## Success Criteria

Analysis is complete when ALL of the following are true:

1. ✅ All code paths producing symptom have been traced and analyzed
2. ✅ Working reference implementations have been identified and compared
3. ✅ ALL divergences have been categorized (bug vs intentional)
4. ✅ Each identified issue's necessity has been validated with causal chain
5. ✅ Analysis explains why partial fixes would fail
6. ✅ Exact file:line locations provided for each issue
7. ✅ Diff-style before/after code blocks created for each fix
8. ✅ Numbered implementation steps documented
9. ✅ Testing verification steps included
10. ✅ Output follows required Markdown format template
11. ✅ Completeness checklist is fully verified
12. ✅ Developer can implement fixes confidently from your documentation

**Only then declare**: "Analysis complete. [N] root causes identified. Developer documentation ready."

---

*Bug Analysis Agent Protocol v1.0*  
*Created: February 2026*  
*Lesson Source: Multi-cause bug pattern analysis*  
*Next Update: After first bug resolution and developer feedback*
