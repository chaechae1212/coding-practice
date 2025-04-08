-- 코드를 입력하세요
SELECT ANIMAL_ID,NAME,if(SEX_UPON_INTAKE like '%intact%','X','O')as '중성화' from animal_ins

;