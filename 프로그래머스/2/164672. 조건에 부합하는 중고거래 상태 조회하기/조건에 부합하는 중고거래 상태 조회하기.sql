-- 코드를 입력하세요
SELECT BOARD_ID,WRITER_ID,TITLE,PRICE,
case
when status='sale' then '판매중'
when status='reserved' then '예약중'
when status='done' then '거래완료'
end
from USED_GOODS_BOARD
where CREATED_DATE='2022-10-05'

order by BOARD_ID desc;