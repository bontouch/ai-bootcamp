# Retrieval & Context Systems (RAG)

## Session Overview
This is an interactive workshop session where we explore how to inject external knowledge into LLMs through Retrieval-Augmented Generation (RAG) patterns.

## Learning Objectives
- Understand LLM knowledge limitations and why external context is needed
- Learn to inject domain-specific knowledge using context formatting
- Implement basic RAG systems with embeddings and vector search
- Practice chunking strategies and semantic retrieval techniques

## What We'll Build Together
1. **Knowledge Gap Discovery**: Test what the LLM doesn't know about Framna
2. **Naive Context Injection**: Add company info as full context using string formatting
3. **Scaling Problems**: Explore limitations of large document injection
4. **RAG Implementation**: Build chunking + embedding + retrieval system
5. **Search Experiments**: Test semantic search with different strategies

## Prerequisites
- OpenAI API key configured
- Basic Python knowledge
- Jupyter notebook environment

## Files
- `rag_workshop.ipynb` - Interactive notebook with progressive code challenges
- `framna_company_info.txt` - Sample company data for testing

## Session Flow
**Duration**: 3 hours (09:00-12:00)

**Structure**:
- 30 min: Challenge 1-2 (Knowledge limits + basic context)
- 45 min: Challenge 3-4 (Scaling problems + RAG setup)  
- 60 min: Challenge 5-6 (Semantic search + complete RAG)
- 30 min: Challenge 7 (Experimentation)
- 15 min: Key takeaways discussion

## Key Concepts Covered
- Context window limitations and costs
- String formatting for prompt templates
- Text chunking strategies
- OpenAI embeddings API
- ChromaDB for vector storage
- Semantic similarity search
- RAG pipeline architecture

## Expected Outcomes
By the end of this session, attendees will understand:
- When and why to use RAG over direct context injection
- How to implement a basic RAG system from scratch
- Trade-offs between retrieval accuracy and computational cost
- Practical considerations for production RAG systems