import json
from services.ocr.schema import PROMPT_CRLV_OCR, CRLVResponse, PROMPT_CNH_OCR, CNHResponse

def gemini_ocr(images, client, is_crlv):
    """
    OCR function using gemini llm

    args:
    - images: image list in PIL format
    - client: gemini LLM client
    - is_crlv: boolean indicating whether it's a crlv image or not
    """

    payload = [PROMPT_CRLV_OCR] + images if is_crlv else [PROMPT_CNH_OCR] + images

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=payload,
        config={
            "response_mime_type": "application/json",
            "response_json_schema": CRLVResponse.model_json_schema() if is_crlv else CNHResponse.model_json_schema(),
        }
    )

    token_usage = response.usage_metadata
    print(f"Entrada (Imagens + Prompt): {token_usage.prompt_token_count} tokens")
    print(f"Saída (Texto gerado):       {token_usage.candidates_token_count} tokens")
    print(f"Total da Requisição:        {token_usage.total_token_count} tokens")

    raw_text = response.text.strip()

    content = json.loads(raw_text)

    content = CRLVResponse(**content) if is_crlv else CNHResponse(**content)

    return content.model_dump()