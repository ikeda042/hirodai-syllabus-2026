from typing import Any

from fastapi import FastAPI, HTTPException

from data import COURSE_DATA


app = FastAPI(
    title="Hirodai Syllabus API",
    description="講義コードから広島大学シラバス情報を取得する API",
    version="1.0.0",
)


def get_course_by_code(course_code: str) -> dict[str, Any]:
    normalized_code = course_code.strip().upper()
    course = COURSE_DATA.get(normalized_code)
    if course is None:
        raise HTTPException(status_code=404, detail=f"Course not found: {normalized_code}")
    return {"course_code": normalized_code, "course": course}


@app.get("/")
def read_root() -> dict[str, Any]:
    return {
        "message": "Hirodai Syllabus API",
        "total_courses": len(COURSE_DATA),
        "example": "/api/courses/WA000101",
        "docs": "/docs",
    }


@app.get("/api/health")
def healthcheck() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/api/courses/{course_code}")
def read_course(course_code: str) -> dict[str, Any]:
    return get_course_by_code(course_code)
