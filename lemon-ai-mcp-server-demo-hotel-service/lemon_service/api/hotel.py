from fastapi import APIRouter
from fastapi import Request
from loguru import logger

from lemon_service.service.image_analysis import ImageAnalysisService

image_analysis_router = APIRouter(prefix="/image-analysis", tags=["AI对图片进行分析的API"])


@image_analysis_router.post("/extract-image-content", summary="提取图片中物品列表")
async def extract_image_content(data: ImageAnalysisExtractImageContent, reqeust: Request = None):
    image_analysis_service = ImageAnalysisService()
    logger.info("用户分析图片-提取图片内容")
    return image_analysis_service.extract_image_content(
        application_id=reqeust.state.application_id,
        image_base64=data.image_base64,
        language=data.language
    )


@image_analysis_router.post("/introduce-image-content", summary="根据图片生成对图片的内容描述")
async def introduce_image_content(data: ImageAnalysisIntroduceImageContent, reqeust: Request = None):
    image_analysis_service = ImageAnalysisService()
    logger.info("用户分析图片-根据图片生成对图片的内容描述")
    return image_analysis_service.introduce_image_content(
        application_id=reqeust.state.application_id,
        image_base64=data.image_base64,
        language=data.language
    )
