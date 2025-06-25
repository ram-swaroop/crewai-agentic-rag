# Example-1
### `python main.py -q "How does DSPy differ from traditional methods of prompting language models in terms of modularity and optimization?"` 

🚀 Crew: crew                                                                                                                                     
├── 📋 Task: 886fc007-efc4-423d-8a25-f430e0209c12                                                                                                 
│   Assigned to: Router                                                                                                                           
│   Status: ✅ Completed                                                                                                                          
│   └── 🔧 Used router_tool (1)                                                                                                                   
├── 📋 Task: be91b956-2a0d-4ef1-beba-8b4be4c671c4                                                                                                 
│   Assigned to: Information Retriever                                                                                                            
│   Status: ✅ Completed                                                                                                                          
│   └── 🔧 Used rag_tool (1)                                                                                                                      
├── 📋 Task: b4037fcc-f0b2-4111-8630-4896d2acd7e2                                                                                                 
│   Assigned to: Answer Grader                                                                                                                    
│   Status: ✅ Completed                                                                                                                          
└── 📋 Task: 8a3b7f7d-0895-420e-a0f8-0773d8df23f6                                                                                                 
    Assigned to: Hallucination Grader                                                                                                             
    Status: ✅ Completed

### Agent: Final Answer Generator                                                                                                                   
#### Final Answer:
DSPy differs from traditional prompting by using parameterized declarative modules that can be composed and optimized with training optimizers,   
unlike the hand-tuning required in traditional prompting. DSPy's modules are task-adaptive and learn desired behaviors through iterative
bootstrapping, while its compiler optimizes pipelines of these modules, creating self-improving NLP systems without hand-crafted prompts.


# Example-2
### `python main.py -q "How does DSPy compare to existing libraries like LangChain and LlamaIndex in terms of prompt engineering and modularity?"` 

🚀 Crew: crew                                                                                                                                     
├── 📋 Task: bc79f25e-f383-4d62-b44f-b2e51d9906ca                                                                                                 
│   Assigned to: Router                                                                                                                           
│   Status: ✅ Completed                                                                                                                          
│   └── 🔧 Used router_tool (1)                                                                                                                   
├── 📋 Task: f6bac0e1-1611-47cf-9679-a6a9c85ba9c4                                                                                                 
│   Assigned to: Information Retriever                                                                                                            
│   Status: ✅ Completed                                                                                                                          
│   └── 🔧 Used rag_tool (1)                                                                                                                      
├── 📋 Task: ecd869df-4b32-454a-b9aa-0353fb010790                                                                                                 
│   Assigned to: Answer Grader                                                                                                                    
│   Status: ✅ Completed                                                                                                                          
├── 📋 Task: 7236b8f3-7092-405a-b7e3-7d983f428ce1                                                                                                 
│   Assigned to: Hallucination Grader                                                                                                             
│   Status: ✅ Completed                                                                                                                          
└── 📋 Task: 92442c9c-0119-46ee-99ad-29c5b48df3d1                                                                                                 
    Assigned to: Final Answer Generator                                                                                                           
    Status: ✅ Completed

### Agent: Final Answer Generator                                                                                                                   
#### Final Answer:                                                                                                                                  
DSPy uses a structured framework that automatically bootstraps prompts, avoiding hand-written prompts, unlike LangChain and LlamaIndex, which rely
on manual prompt engineering. DSPy introduces core composable operators for building and optimizing LM pipelines, focusing on automatic           
compilation and self-improvement, while existing libraries offer off-the-shelf higher-level abstractions.                                         


# Example-3:
### `python main.py -q "Which teams qualified for round-16 in recent fifa club worldcup?"`               
                                                                                                                                                 
🚀 Crew: crew                                                                                                                                     
├── 📋 Task: 09e50fc2-b840-4520-bf82-645dae244fb9                                                                                                 
│   Assigned to: Router                                                                                                                           
│   Status: ✅ Completed                                                                                                                          
│   └── 🔧 Used router_tool (1)                                                                                                                   
├── 📋 Task: 49e3d2ef-1b56-412d-b4b0-2c8be1f45316                                                                                                 
│   Assigned to: Information Retriever                                                                                                            
│   Status: ✅ Completed                                                                                                                          
│   ├── 🔧 Used web_search_tool (1)                                                                                                               
│   └── 🔧 Used web_search_tool (2)                                                                                                               
├── 📋 Task: 887e594a-ef22-4df0-9301-0cc70bb2baf0                                                                                                 
│   Assigned to: Answer Grader                                                                                                                    
│   Status: ✅ Completed                                                                                                                          
├── 📋 Task: 4d6eaa86-bfd8-4fe2-83af-1c87451614c7                                                                                                 
│   Assigned to: Hallucination Grader                                                                                                             
│   Status: ✅ Completed                                                                                                                          
└── 📋 Task: b263064d-6273-43f4-a2d5-506c4aa476a2                                                                                                 
    Assigned to: Final Answer Generator                                                                                                           
    Status: ✅ Completed                                                                                                                          
    └── 🔧 Used web_search_tool (3)
### Agent: Final Answer Generator
#### Final Answer:                                                                                                                                  
The FIFA Club World Cup 2025 will feature 32 teams. Qualification is ongoing. Here are some of the qualified teams:                               
                                                                                                                                                  
*   **UEFA (Europe):** Chelsea, Real Madrid, Manchester City                                                                                      
*   **CONMEBOL (South America):** Palmeiras, Flamengo, Fluminense                                                                                 
*   **AFC (Asia):** Al Hilal, Urawa Red Diamonds, Al Ahly                                                                                         
*   **CAF (Africa):** Wydad Casablanca, Al Ahly                                                                                                   
*   **CONCACAF (North America):** Monterrey, Seattle Sounders, Club Leon                                                                          
*   **OFC (Oceania):** Auckland City                                                                                                              
                                                                                                                                                  
For a complete and up-to-date list, refer to the official FIFA website or other reputable sports news outlets.                                                                       


## 🔍 Observation

- ⚠️ **Answer for Example 3 is inaccurate** due to the use of **summarized content** returned by `TavilySearchResults`.
- ✅ A potential solution is to enable `raw_content` in the search response and implement logic to **extract only the most relevant context** from the full content, rather than relying on pre-summarized results.
