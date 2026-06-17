from crewai import Task
from agents import (
    create_ceo_agent,
    create_cfo_agent,
    create_coo_agent,
    create_cqo_agent,
    create_supply_chain_agent,
    create_engineering_agent,
    create_devils_advocate_agent,
    create_production_agent,
    create_rd_director_agent,
    create_military_user_agent,
    create_auditor_agent,
)


def create_all_tasks(topic: str):
    """Create all board tasks for a given topic"""
    
    # Create agents
    ceo = create_ceo_agent()
    cfo = create_cfo_agent()
    coo = create_coo_agent()
    cqo = create_cqo_agent()
    supply_chain = create_supply_chain_agent()
    engineering = create_engineering_agent()
    devils_advocate = create_devils_advocate_agent()
    production = create_production_agent()
    rd_director = create_rd_director_agent()
    military_user = create_military_user_agent()
    auditor = create_auditor_agent()
    
    # Strategic Planning Task
    strategic_planning_task = Task(
        description=f"""Analyze the following topic and provide strategic recommendations:
        {topic}
        
        Consider market opportunities, competitive landscape, and long-term viability.
        Provide a comprehensive strategic plan with clear objectives and milestones.""",
        agent=ceo,
        expected_output="Comprehensive strategic plan with objectives, milestones, and key success factors."
    )
    
    # Financial Analysis Task
    financial_task = Task(
        description=f"""Conduct financial analysis for the proposed strategy:
        {topic}
        
        Analyze costs, ROI, cash flow implications, and financial risks.
        Provide financial projections and budget requirements.""",
        agent=cfo,
        expected_output="Detailed financial analysis including projections, budget requirements, and ROI calculations."
    )
    
    # Operational Optimization Task
    operational_task = Task(
        description=f"""Assess operational implications and optimization opportunities:
        {topic}
        
        Identify process improvements, efficiency gains, and operational risks.
        Propose operational excellence initiatives.""",
        agent=coo,
        expected_output="Operational assessment with efficiency recommendations and process improvements."
    )
    
    # Quality and Compliance Task
    quality_task = Task(
        description=f"""Evaluate quality and compliance requirements:
        {topic}
        
        Assess regulatory compliance, quality standards, and risk mitigation measures.
        Ensure adherence to all applicable regulations and standards.""",
        agent=cqo,
        expected_output="Quality and compliance assessment with regulatory requirements and standards."
    )
    
    # Supply Chain Optimization Task
    supply_chain_task = Task(
        description=f"""Optimize supply chain and logistics strategy:
        {topic}
        
        Assess vendor relationships, logistics efficiency, and supply chain resilience.
        Identify optimization opportunities and potential bottlenecks.""",
        agent=supply_chain,
        expected_output="Supply chain optimization strategy with vendor management and logistics improvements."
    )
    
    # Engineering Feasibility Task
    engineering_task = Task(
        description=f"""Assess technical feasibility and innovation opportunities:
        {topic}
        
        Evaluate technical requirements, technology solutions, and innovation potential.
        Propose technical architecture and innovation initiatives.""",
        agent=engineering,
        expected_output="Technical feasibility assessment with architectural recommendations and innovation opportunities."
    )
    
    # Risk Assessment Task
    risk_task = Task(
        description=f"""Provide critical analysis and identify potential risks:
        {topic}
        
        Challenge assumptions, identify weaknesses, and highlight unintended consequences.
        Provide contingency planning and risk mitigation strategies.""",
        agent=devils_advocate,
        expected_output="Critical risk assessment with contingency plans and risk mitigation strategies."
    )
    
    # Production Strategy Task
    production_task = Task(
        description=f"""Develop production strategy and manufacturing plan:
        {topic}
        
        Assess manufacturing requirements, production efficiency, and scalability.
        Propose production optimization and capacity planning.""",
        agent=production,
        expected_output="Production strategy with manufacturing plan and efficiency improvements."
    )
    
    # R&D Strategy Task
    rd_task = Task(
        description=f"""Develop research and development strategy:
        {topic}
        
        Identify innovation opportunities, R&D investments, and product development roadmap.
        Propose breakthrough innovations and continuous improvement initiatives.""",
        agent=rd_director,
        expected_output="R&D strategy with innovation roadmap and product development plans."
    )
    
    # Military Requirements Task
    military_task = Task(
        description=f"""Assess military and defense sector requirements:
        {topic}
        
        Evaluate defense standards, security requirements, and operational specifications.
        Ensure alignment with military protocols and specifications.""",
        agent=military_user,
        expected_output="Military requirements assessment with defense standards and security specifications."
    )
    
    # Audit and Validation Task
    audit_task = Task(
        description=f"""Conduct independent audit and validation:
        {topic}
        
        Review all recommendations, validate against facts and regulations.
        Provide objective assessment and validation of proposed decisions.""",
        agent=auditor,
        expected_output="Independent audit report with validation of decisions and recommendations."
    )
    
    return [
        strategic_planning_task,
        financial_task,
        operational_task,
        quality_task,
        supply_chain_task,
        engineering_task,
        risk_task,
        production_task,
        rd_task,
        military_task,
        audit_task,
    ]
