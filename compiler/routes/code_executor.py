from fastapi import APIRouter, HTTPException
from compiler.models import CodeInput

router = APIRouter()

@router.post("/execute_code/")
async def execute_code_endpoint(code_input: CodeInput):
    try:
        # Import execute_code here to avoid circular import
        from compiler.services.code_executor_service import execute_code
        result = execute_code(code_input.code)
        return {"output": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
