select animal_id, name
from animal_outs
where animal_id not in (select animal_id 
                        from animal_ins);




# ins = 보호소에 들어온 동물의 정보 테이블
# outs = 입양 보낸 동물의 정보 테이블
