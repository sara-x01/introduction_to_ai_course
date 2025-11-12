<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Course Project: RoboMind | SE444</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600&family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.3.0/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <style>
        :root {
            --primary-color: #0a2540;
            --secondary-color: #635bff;
            --accent-color: #00d4ff;
            --success-color: #32D583;
            --warning-color: #ffc107;
            --danger-color: #dc3545;
            --text-color: #424770;
            --light-bg: #f6f9fc;
        }

        body {
            font-family: 'Poppins', sans-serif;
            background: var(--light-bg);
            color: var(--text-color);
            line-height: 1.6;
        }

        .header {
            background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
            color: white;
            padding: 2rem 0;
            margin-bottom: 1.5rem;
        }

        .back-link {
            color: white;
            text-decoration: none;
            opacity: 0.9;
            transition: opacity 0.3s;
        }

        .back-link:hover {
            opacity: 1;
            color: white;
        }

        .content-section {
            background: white;
            border-radius: 12px;
            padding: 1.5rem;
            margin-bottom: 1.5rem;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
        }

        .section-header {
            background: linear-gradient(135deg, var(--secondary-color), var(--accent-color));
            color: white;
            padding: 1rem 1.5rem;
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.3s;
            margin-bottom: 0;
        }

        .section-header:hover {
            transform: translateX(5px);
            box-shadow: 0 4px 12px rgba(99, 91, 255, 0.3);
        }

        .section-header h2 {
            color: white;
            margin: 0;
            display: flex;
            align-items: center;
            justify-content: space-between;
            font-size: 1.3rem;
        }

        .info-box {
            background: linear-gradient(135deg, rgba(0, 212, 255, 0.1), rgba(50, 213, 131, 0.1));
            border-left: 4px solid var(--accent-color);
            padding: 1rem;
            border-radius: 8px;
            margin: 0.75rem 0;
        }

        .warning-box {
            background: linear-gradient(135deg, rgba(255, 193, 7, 0.1), rgba(255, 152, 0, 0.1));
            border-left: 4px solid var(--warning-color);
            padding: 1rem;
            border-radius: 8px;
            margin: 0.75rem 0;
        }

        .danger-box {
            background: linear-gradient(135deg, rgba(244, 67, 54, 0.1), rgba(220, 53, 69, 0.1));
            border-left: 4px solid var(--danger-color);
            padding: 1rem;
            border-radius: 8px;
            margin: 0.75rem 0;
        }

        .success-box {
            background: linear-gradient(135deg, rgba(50, 213, 131, 0.1), rgba(40, 167, 69, 0.1));
            border-left: 4px solid var(--success-color);
            padding: 1rem;
            border-radius: 8px;
            margin: 0.75rem 0;
        }

        .phase-card {
            border: 2px solid #dee2e6;
            border-radius: 10px;
            padding: 1.25rem;
            margin-bottom: 1rem;
            transition: all 0.3s;
        }

        .phase-card:hover {
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
            transform: translateY(-2px);
        }

        .phase-number {
            width: 45px;
            height: 45px;
            border-radius: 50%;
            background: linear-gradient(135deg, var(--secondary-color), var(--accent-color));
            color: white;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 700;
            font-size: 1.3rem;
            margin-right: 1rem;
            flex-shrink: 0;
        }

        .download-btn {
            background: linear-gradient(135deg, var(--secondary-color), var(--accent-color));
            color: white;
            border: none;
            padding: 0.75rem 1.5rem;
            border-radius: 8px;
            font-weight: 600;
            transition: all 0.3s;
            text-decoration: none;
            display: inline-block;
        }

        .download-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(99, 91, 255, 0.3);
            color: white;
        }

        .table-responsive {
            margin: 1rem 0;
        }

        .table {
            margin-bottom: 0;
        }

        .badge-phase {
            padding: 0.5rem 0.75rem;
            font-size: 0.85rem;
            font-weight: 600;
        }

        .ai-policy-section {
            background: linear-gradient(135deg, rgba(244, 67, 54, 0.05), rgba(255, 193, 7, 0.05));
            border: 3px solid var(--danger-color);
            border-radius: 12px;
            padding: 1.5rem;
            margin: 1.5rem 0;
        }

        .ai-policy-section h3 {
            color: var(--danger-color);
            margin-bottom: 1rem;
        }

        .policy-item {
            display: flex;
            align-items: start;
            margin-bottom: 1rem;
            padding: 0.75rem;
            background: white;
            border-radius: 8px;
        }

        .policy-icon {
            font-size: 1.5rem;
            margin-right: 1rem;
            flex-shrink: 0;
        }

        .icon-allowed {
            color: var(--success-color);
        }

        .icon-forbidden {
            color: var(--danger-color);
        }

        .icon-warning {
            color: var(--warning-color);
        }
    </style>
</head>

<body>
    <div class="header">
        <div class="container">
            <a href="../index.php" class="back-link">
                <i class="fas fa-arrow-left"></i> Back to SE444 Course
            </a>
            <h1 class="mt-3"><i class="fas fa-robot me-2"></i>Course Project: RoboMind</h1>
            <p class="lead">Build a Rational AI Agent - Integrating Search, Logic, and Probability</p>
        </div>
    </div>

    <div class="container mb-5">

        <!-- Urgent Timeline Alert -->
        <div class="alert alert-danger border-danger" style="border-width: 3px !important; border-left-width: 8px !important;">
            <div class="d-flex align-items-center">
                <div style="font-size: 3rem; margin-right: 1rem;"><i class="fas fa-clock"></i></div>
                <div>
                    <h4 class="alert-heading mb-2"><i class="fas fa-exclamation-triangle me-2"></i>URGENT: 3-Week Deadline!</h4>
                    <p class="mb-2">
                        <strong>You have ONLY 3 WEEKS</strong> to complete all 4 phases of this project + report.
                        This is an intensive timeline that requires immediate action.
                    </p>
                    <hr>
                    <p class="mb-0">
                        <strong>Recommended Schedule:</strong><br>
                        📅 <strong>Week 1:</strong> Search Algorithms (Phase 1) - 25 points<br>
                        📅 <strong>Week 2:</strong> Logic + Probability (Phases 2 & 3) - 40 points<br>
                        📅 <strong>Week 3:</strong> Integration + Report (Phase 4 + Report) - 35 points<br>
                        <span style="color: #721c24; font-weight: 700;">⚠️ NO EXTENSIONS - START TODAY!</span>
                    </p>
                </div>
            </div>
        </div>

        <!-- Project Overview -->
        <div class="content-section">
            <h2 class="mb-3"><i class="fas fa-info-circle me-2" style="color: var(--secondary-color);"></i>Project Overview</h2>

            <div class="info-box">
                <h5><i class="fas fa-target me-2"></i>What You'll Build</h5>
                <p class="mb-2">
                    You will implement a <strong>rational AI agent</strong> that navigates a 2D grid world using Python and Pygame.
                    Your agent will integrate three key AI reasoning techniques learned in this course:
                </p>
                <ul class="mb-0">
                    <li><strong>Search Algorithms</strong> (BFS, UCS, A*) - to plan optimal paths</li>
                    <li><strong>Logical Reasoning</strong> (Knowledge Base + Inference) - to reason about the world</li>
                    <li><strong>Probabilistic Reasoning</strong> (Bayes' Rule) - to handle uncertainty</li>
                </ul>
            </div>

            <div class="row mt-3">
                <div class="col-md-4">
                    <div class="text-center p-3 border rounded">
                        <div style="font-size: 3rem; color: var(--secondary-color);">🤖</div>
                        <h6 class="mt-2">Intelligent Agent</h6>
                        <p class="small text-muted mb-0">Plans, reasons, and adapts</p>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="text-center p-3 border rounded">
                        <div style="font-size: 3rem; color: var(--accent-color);">🎮</div>
                        <h6 class="mt-2">Visual Simulation</h6>
                        <p class="small text-muted mb-0">Pygame grid world</p>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="text-center p-3 border rounded">
                        <div style="font-size: 3rem; color: var(--success-color);">📈</div>
                        <h6 class="mt-2">Performance Analysis</h6>
                        <p class="small text-muted mb-0">Compare algorithms</p>
                    </div>
                </div>
            </div>

            <div class="success-box mt-3">
                <h6><i class="fas fa-graduation-cap me-2"></i>Learning Outcomes</h6>
                <p class="small mb-1">By completing this project, you will:</p>
                <ol class="small mb-0">
                    <li>Implement and compare classical search algorithms</li>
                    <li>Apply propositional logic for automated reasoning</li>
                    <li>Use Bayesian inference to handle sensor uncertainty</li>
                    <li>Build a complete rational agent integrating all techniques</li>
                    <li>Analyze and evaluate agent performance systematically</li>
                </ol>
            </div>
        </div>

        <!-- Project Phases -->
        <div class="content-section">
            <h2 class="mb-3"><i class="fas fa-tasks me-2" style="color: var(--secondary-color);"></i>Project Phases</h2>

            <div class="danger-box">
                <h6><i class="fas fa-calendar-alt me-2"></i>Timeline: 3 WEEKS ONLY - START IMMEDIATELY!</h6>
                <p class="small mb-0">
                    The project is divided into 4 phases to be completed in just 3 weeks.
                    <strong style="color: var(--danger-color);">This is a tight deadline - START TODAY!</strong>
                    Focus on getting core functionality working first, then refine.
                </p>
            </div>

            <!-- Phase 1 -->
            <div class="phase-card">
                <div class="d-flex align-items-start">
                    <div class="phase-number">1</div>
                    <div class="flex-grow-1">
                        <div class="d-flex justify-content-between align-items-center">
                            <h4 class="mb-2" style="color: var(--secondary-color);">Search Algorithms</h4>
                            <span class="badge bg-primary badge-phase">Week 1 • 25 points</span>
                        </div>
                        <p class="mb-2">
                            Implement three search algorithms to find paths from start to goal.
                        </p>
                        <div class="row">
                            <div class="col-md-6">
                                <strong>What to Implement:</strong>
                                <ul class="small mb-2">
                                    <li><strong>BFS</strong> - Breadth-First Search (shortest path in steps)</li>
                                    <li><strong>UCS</strong> - Uniform Cost Search (lowest cost path)</li>
                                    <li><strong>A*</strong> - A* with Manhattan & Euclidean heuristics</li>
                                </ul>
                            </div>
                            <div class="col-md-6">
                                <strong>Files to Modify:</strong>
                                <ul class="small mb-2">
                                    <li><code>ai_core/search_algorithms.py</code></li>
                                    <li><code>agents/search_agent.py</code></li>
                                </ul>
                                <strong>Test Command:</strong>
                                <div class="bg-light p-2 rounded mt-1">
                                    <code>python main.py --test-search</code>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Phase 2 -->
            <div class="phase-card">
                <div class="d-flex align-items-start">
                    <div class="phase-number">2</div>
                    <div class="flex-grow-1">
                        <div class="d-flex justify-content-between align-items-center">
                            <h4 class="mb-2" style="color: var(--success-color);">Logic-Based Reasoning</h4>
                            <span class="badge bg-success badge-phase">Week 2 • 20 points</span>
                        </div>
                        <p class="mb-2">
                            Implement a knowledge base with propositional logic and forward chaining inference.
                        </p>
                        <div class="row">
                            <div class="col-md-6">
                                <strong>What to Implement:</strong>
                                <ul class="small mb-2">
                                    <li><strong>Knowledge Base</strong> - Store facts and rules</li>
                                    <li><strong>Forward Chaining</strong> - Automatic inference</li>
                                    <li><strong>Logic Agent</strong> - Reason about safe moves</li>
                                </ul>
                            </div>
                            <div class="col-md-6">
                                <strong>Files to Modify:</strong>
                                <ul class="small mb-2">
                                    <li><code>ai_core/knowledge_base.py</code></li>
                                    <li><code>agents/logic_agent.py</code></li>
                                </ul>
                                <strong>Test Command:</strong>
                                <div class="bg-light p-2 rounded mt-1">
                                    <code>python main.py --test-logic</code>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Phase 3 -->
            <div class="phase-card">
                <div class="d-flex align-items-start">
                    <div class="phase-number">3</div>
                    <div class="flex-grow-1">
                        <div class="d-flex justify-content-between align-items-center">
                            <h4 class="mb-2" style="color: var(--warning-color);">Probabilistic Reasoning</h4>
                            <span class="badge bg-warning text-dark badge-phase">Week 2-3 • 20 points</span>
                        </div>
                        <p class="mb-2">
                            Implement Bayesian belief updates to handle sensor uncertainty and noisy readings.
                        </p>
                        <div class="row">
                            <div class="col-md-6">
                                <strong>What to Implement:</strong>
                                <ul class="small mb-2">
                                    <li><strong>Bayes' Rule</strong> - P(H|E) calculations</li>
                                    <li><strong>Belief Updates</strong> - Handle sensor noise</li>
                                    <li><strong>Probabilistic Agent</strong> - Navigate under uncertainty</li>
                                </ul>
                            </div>
                            <div class="col-md-6">
                                <strong>Files to Modify:</strong>
                                <ul class="small mb-2">
                                    <li><code>ai_core/bayes_reasoning.py</code></li>
                                    <li><code>agents/probabilistic_agent.py</code></li>
                                </ul>
                                <strong>Test Command:</strong>
                                <div class="bg-light p-2 rounded mt-1">
                                    <code>python main.py --test-probability</code>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Phase 4 -->
            <div class="phase-card">
                <div class="d-flex align-items-start">
                    <div class="phase-number">4</div>
                    <div class="flex-grow-1">
                        <div class="d-flex justify-content-between align-items-center">
                            <h4 class="mb-2" style="color: var(--accent-color);">Hybrid Integration</h4>
                            <span class="badge bg-info badge-phase">Week 3 • 20 points</span>
                        </div>
                        <p class="mb-2">
                            Integrate all three reasoning techniques into a single rational agent.
                        </p>
                        <div class="row">
                            <div class="col-md-6">
                                <strong>What to Implement:</strong>
                                <ul class="small mb-2">
                                    <li><strong>Integrated Decision-Making</strong> - Combine all techniques</li>
                                    <li><strong>Strategy Selection</strong> - Choose appropriate method</li>
                                    <li><strong>Rational Behavior</strong> - Optimize performance</li>
                                </ul>
                            </div>
                            <div class="col-md-6">
                                <strong>Files to Modify:</strong>
                                <ul class="small mb-2">
                                    <li><code>agents/hybrid_agent.py</code></li>
                                </ul>
                                <strong>Test Command:</strong>
                                <div class="bg-light p-2 rounded mt-1">
                                    <code>python main.py --test-hybrid</code>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- AI Usage Policy -->
        <div class="ai-policy-section">
            <h3><i class="fas fa-exclamation-triangle me-2"></i>AI Usage Policy - READ CAREFULLY</h3>

            <div class="danger-box mb-3">
                <h5><i class="fas fa-robot me-2"></i>Permitted vs. Prohibited AI Use</h5>
                <p class="mb-0">
                    This project is designed to assess <strong>YOUR understanding</strong> of AI algorithms.
                    While AI tools can be helpful, they <strong>MUST NOT</strong> write your code for you.
                </p>
            </div>

            <div class="policy-item">
                <div class="policy-icon icon-allowed"><i class="fas fa-check-circle"></i></div>
                <div>
                    <h6 class="mb-1" style="color: var(--success-color);">✓ ALLOWED: Code Autocompletion</h6>
                    <p class="small mb-0">
                        You may use IDE features like GitHub Copilot, TabNine, or similar tools for
                        <strong>autocompletion and syntax suggestions</strong>. These should complete partial lines or suggest next steps.
                    </p>
                </div>
            </div>

            <div class="policy-item">
                <div class="policy-icon icon-allowed"><i class="fas fa-check-circle"></i></div>
                <div>
                    <h6 class="mb-1" style="color: var(--success-color);">✓ ALLOWED: LLM for Guidance & Explanation</h6>
                    <p class="small mb-0">
                        You may ask ChatGPT, Claude, or similar LLMs to <strong>explain concepts</strong>,
                        <strong>clarify algorithms</strong>, or help you understand errors. Example:
                        "Explain how BFS works" or "Why am I getting this Python error?"
                    </p>
                </div>
            </div>

            <div class="policy-item">
                <div class="policy-icon icon-allowed"><i class="fas fa-check-circle"></i></div>
                <div>
                    <h6 class="mb-1" style="color: var(--success-color);">✓ ALLOWED: Debugging Assistance</h6>
                    <p class="small mb-0">
                        You may use AI to help <strong>debug specific errors</strong> or understand why your code doesn't work.
                        Always understand the fix before applying it!
                    </p>
                </div>
            </div>

            <div class="policy-item">
                <div class="policy-icon icon-forbidden"><i class="fas fa-times-circle"></i></div>
                <div>
                    <h6 class="mb-1" style="color: var(--danger-color);">✗ FORBIDDEN: Generating Complete Functions</h6>
                    <p class="small mb-0">
                        <strong>DO NOT</strong> ask AI to "write BFS algorithm" or "implement A* search" and copy the result.
                        This defeats the learning purpose and <strong>will be detected</strong>.
                    </p>
                </div>
            </div>

            <div class="policy-item">
                <div class="policy-icon icon-forbidden"><i class="fas fa-times-circle"></i></div>
                <div>
                    <h6 class="mb-1" style="color: var(--danger-color);">✗ FORBIDDEN: Copy-Pasting Large Code Blocks</h6>
                    <p class="small mb-0">
                        <strong>DO NOT</strong> copy entire functions, classes, or algorithms from AI assistants, Stack Overflow,
                        GitHub, or other sources without understanding and significantly modifying them.
                    </p>
                </div>
            </div>

            <div class="policy-item">
                <div class="policy-icon icon-forbidden"><i class="fas fa-times-circle"></i></div>
                <div>
                    <h6 class="mb-1" style="color: var(--danger-color);">✗ FORBIDDEN: Submitting AI-Written Code</h6>
                    <p class="small mb-0">
                        Any substantial portions of code that are <strong>clearly AI-generated</strong> (detected by our analysis tools)
                        will result in zero points for that phase and potential academic integrity violations.
                    </p>
                </div>
            </div>

            <div class="danger-box mt-3">
                <h6><i class="fas fa-shield-alt me-2"></i>AI Detection & Enforcement</h6>
                <div class="row">
                    <div class="col-md-6">
                        <p class="small mb-2"><strong>We will use:</strong></p>
                        <ul class="small mb-0">
                            <li>AI-generated code detection tools</li>
                            <li>Code analysis agents to identify patterns</li>
                            <li>Manual review of submissions</li>
                            <li>Oral examinations if needed</li>
                        </ul>
                    </div>
                    <div class="col-md-6">
                        <p class="small mb-2"><strong>Penalties:</strong></p>
                        <ul class="small mb-0">
                            <li><strong>Minor violations:</strong> Resubmit with deduction</li>
                            <li><strong>Extensive AI-generated code:</strong> Zero on project</li>
                            <li><strong>Repeated violations:</strong> Academic integrity case</li>
                            <li><strong>Failure to explain code:</strong> Zero on project</li>
                        </ul>
                    </div>
                </div>
            </div>

            <div class="success-box mt-3">
                <h6><i class="fas fa-lightbulb me-2"></i>How to Use AI Responsibly</h6>
                <ol class="small mb-0">
                    <li><strong>Learn first, code second:</strong> Understand the algorithm before implementing</li>
                    <li><strong>Start from scratch:</strong> Write your own code structure</li>
                    <li><strong>Use AI for hints:</strong> Not complete solutions</li>
                    <li><strong>Understand every line:</strong> Be able to explain your code</li>
                    <li><strong>Add personal touches:</strong> Use your own variable names, comments, style</li>
                    <li><strong>Cite when appropriate:</strong> If you got a key idea from AI, mention it in comments</li>
                </ol>
            </div>
        </div>

        <!-- Grading Rubric -->
        <div class="content-section">
            <h2 class="mb-3"><i class="fas fa-clipboard-check me-2" style="color: var(--secondary-color);"></i>Grading Rubric (100 Points)</h2>

            <div class="table-responsive">
                <table class="table table-bordered">
                    <thead style="background: linear-gradient(135deg, var(--secondary-color), var(--accent-color)); color: white;">
                        <tr>
                            <th style="width: 25%;">Component</th>
                            <th style="width: 10%;">Points</th>
                            <th style="width: 65%;">Criteria</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td><strong>Phase 1: Search</strong></td>
                            <td class="text-center"><strong>25</strong></td>
                            <td>
                                <small>
                                    • BFS correctness & efficiency (8 pts)<br>
                                    • UCS correctness & efficiency (8 pts)<br>
                                    • A* correctness & optimality (9 pts)
                                </small>
                            </td>
                        </tr>
                        <tr>
                            <td><strong>Phase 2: Logic</strong></td>
                            <td class="text-center"><strong>20</strong></td>
                            <td>
                                <small>
                                    • Knowledge base implementation (10 pts)<br>
                                    • Forward chaining inference (10 pts)
                                </small>
                            </td>
                        </tr>
                        <tr>
                            <td><strong>Phase 3: Probability</strong></td>
                            <td class="text-center"><strong>20</strong></td>
                            <td>
                                <small>
                                    • Bayes' rule implementation (10 pts)<br>
                                    • Belief map updates (10 pts)
                                </small>
                            </td>
                        </tr>
                        <tr>
                            <td><strong>Phase 4: Integration</strong></td>
                            <td class="text-center"><strong>20</strong></td>
                            <td>
                                <small>
                                    • Hybrid agent integration (15 pts)<br>
                                    • Rational behavior demonstration (5 pts)
                                </small>
                            </td>
                        </tr>
                        <tr>
                            <td><strong>Report & Analysis</strong></td>
                            <td class="text-center"><strong>10</strong></td>
                            <td>
                                <small>
                                    • Clear explanation of approach (3 pts)<br>
                                    • Experimental results & graphs (4 pts)<br>
                                    • Reflection & discussion (3 pts)
                                </small>
                            </td>
                        </tr>
                        <tr>
                            <td><strong>Code Quality</strong></td>
                            <td class="text-center"><strong>5</strong></td>
                            <td>
                                <small>
                                    • Well-commented code (2 pts)<br>
                                    • Proper structure & naming (2 pts)<br>
                                    • Follows Python conventions (1 pt)
                                </small>
                            </td>
                        </tr>
                        <tr style="background: #f8f9fa; font-weight: 700;">
                            <td><strong>TOTAL</strong></td>
                            <td class="text-center"><strong>100</strong></td>
                            <td></td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>

        <!-- Submission Requirements -->
        <div class="content-section">
            <h2 class="mb-3"><i class="fas fa-file-upload me-2" style="color: var(--secondary-color);"></i>Submission Requirements</h2>

            <div class="row">
                <div class="col-md-6">
                    <div class="info-box">
                        <h6><i class="fas fa-code me-2"></i>Code Submission</h6>
                        <ul class="small mb-0">
                            <li>Complete <code>RoboMind/</code> folder (ZIP file)</li>
                            <li>All Python files with your implementations</li>
                            <li>Include test maps if you created new ones</li>
                            <li>Remove <code>__pycache__</code> folders before zipping</li>
                        </ul>
                    </div>
                </div>
                <div class="col-md-6">
                    <div class="info-box">
                        <h6><i class="fas fa-file-pdf me-2"></i>Report Submission (PDF)</h6>
                        <ul class="small mb-0">
                            <li>5-10 pages (not including code appendix)</li>
                            <li>Include performance graphs and tables</li>
                            <li>Explain your approach for each phase</li>
                            <li>Discuss results and limitations</li>
                        </ul>
                    </div>
                </div>
            </div>

            <div class="danger-box mt-3">
                <h6><i class="fas fa-calendar me-2"></i>Important Dates - TIGHT DEADLINE!</h6>
                <div class="table-responsive">
                    <table class="table table-sm mb-0">
                        <tr>
                            <td style="width: 30%;"><strong>Week 1 Target</strong></td>
                            <td>Phase 1 (Search) - Get BFS, UCS, A* working</td>
                        </tr>
                        <tr>
                            <td><strong>Week 2 Target</strong></td>
                            <td>Phases 2 & 3 (Logic + Probability) - Complete KB and Bayes</td>
                        </tr>
                        <tr>
                            <td><strong>Week 3 Target</strong></td>
                            <td>Phase 4 (Integration) + Report writing</td>
                        </tr>
                        <tr style="background: #ffebee; border: 2px solid var(--danger-color);">
                            <td><strong>⚠️ FINAL DEADLINE</strong></td>
                            <td><strong>END OF WEEK 3 - All phases + Report (NO EXTENSIONS!)</strong></td>
                        </tr>
                    </table>
                </div>
                <p class="small mt-2 mb-0" style="color: var(--danger-color); font-weight: 600;">
                    <i class="fas fa-exclamation-triangle me-1"></i>
                    Late submissions will NOT be accepted. Plan accordingly and START IMMEDIATELY!
                </p>
            </div>
        </div>

        <!-- Download Project -->
        <div class="content-section text-center">
            <h2 class="mb-3"><i class="fas fa-download me-2" style="color: var(--secondary-color);"></i>Get Started</h2>

            <div class="info-box">
                <h5><i class="fas fa-rocket me-2"></i>Ready to Begin?</h5>
                <p class="mb-3">
                    Download the starter code package and follow the instructions in <code>QUICKSTART.md</code>
                </p>
                <a href="RoboMind/" class="download-btn me-2">
                    <i class="fas fa-folder-open me-2"></i>View Project Files
                </a>
                <a href="RoboMind/README.md" class="download-btn me-2">
                    <i class="fas fa-book me-2"></i>Read Full Documentation
                </a>
                <a href="RoboMind/QUICKSTART.md" class="download-btn">
                    <i class="fas fa-bolt me-2"></i>Quick Start Guide
                </a>
            </div>

            <div class="warning-box mt-4">
                <h6><i class="fas fa-question-circle me-2"></i>Need Help?</h6>
                <div class="row">
                    <div class="col-md-4">
                        <p class="small mb-1"><strong>Office Hours:</strong></p>
                        <p class="small mb-0">[Schedule TBD]</p>
                    </div>
                    <div class="col-md-4">
                        <p class="small mb-1"><strong>Discussion Forum:</strong></p>
                        <p class="small mb-0">[Link TBD]</p>
                    </div>
                    <div class="col-md-4">
                        <p class="small mb-1"><strong>Email:</strong></p>
                        <p class="small mb-0">[Instructor Email]</p>
                    </div>
                </div>
            </div>
        </div>

        <!-- Academic Integrity -->
        <div class="content-section">
            <h2 class="mb-3"><i class="fas fa-balance-scale me-2" style="color: var(--danger-color);"></i>Academic Integrity</h2>

            <div class="danger-box">
                <h5><i class="fas fa-exclamation-circle me-2"></i>Zero Tolerance Policy</h5>
                <p class="mb-2">
                    This project is an <strong>individual assignment</strong>. Academic dishonesty will not be tolerated.
                </p>
                <div class="row">
                    <div class="col-md-6">
                        <p class="small mb-1"><strong>✓ You MAY:</strong></p>
                        <ul class="small mb-0">
                            <li>Discuss high-level concepts with classmates</li>
                            <li>Ask instructors for clarification</li>
                            <li>Use course materials and textbooks</li>
                            <li>Search for algorithm explanations</li>
                        </ul>
                    </div>
                    <div class="col-md-6">
                        <p class="small mb-1"><strong>✗ You MAY NOT:</strong></p>
                        <ul class="small mb-0">
                            <li>Share code with other students</li>
                            <li>Copy code from online sources</li>
                            <li>Use AI to generate complete solutions</li>
                            <li>Submit work that is not your own</li>
                        </ul>
                    </div>
                </div>
            </div>

            <div class="warning-box mt-3">
                <h6><i class="fas fa-gavel me-2"></i>Consequences of Violations</h6>
                <ul class="small mb-0">
                    <li><strong>First offense:</strong> Zero on project + academic integrity report</li>
                    <li><strong>Repeated violations:</strong> Failure in course + disciplinary action</li>
                    <li><strong>Note:</strong> All cases are reported to the university</li>
                </ul>
            </div>
        </div>

        <!-- Footer -->
        <div class="content-section text-center" style="background: linear-gradient(135deg, rgba(99, 91, 255, 0.05), rgba(0, 212, 255, 0.05));">
            <h4 style="color: var(--secondary-color);"><i class="fas fa-trophy me-2"></i>Build Something Intelligent!</h4>
            <p class="mb-0">
                This project will challenge you, but it's designed to be achievable with consistent effort.
                <br><strong>Start early, test often, and ask for help when needed!</strong>
            </p>
            <hr>
            <small class="text-muted">
                SE444: Artificial Intelligence | Course Project | © 2024
            </small>
        </div>

    </div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.3.0/js/bootstrap.bundle.min.js"></script>
</body>

</html>