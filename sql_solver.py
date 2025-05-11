def get_final_sql_query():
    return """
    SELECT 
        MAX(p.AMOUNT) AS SALARY,
        e.FIRST_NAME || ' ' || e.LAST_NAME AS NAME,
        CAST((julianday('2025-05-11') - julianday(e.DOB)) / 365.25 AS INTEGER) AS AGE,
        d.DEPARTMENT_NAME
    FROM PAYMENTS p
    JOIN EMPLOYEE e ON p.EMP_ID = e.EMP_ID
    JOIN DEPARTMENT d ON e.DEPARTMENT = d.DEPARTMENT_ID
    WHERE strftime('%d', p.PAYMENT_TIME) != '01';
    """