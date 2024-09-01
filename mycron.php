<?php


class RES
{
    public int $value;
    public bool $bump_order;
    
    public function __construct()
    {
        $this->value = 0;
        $this->bump_order = False;
    }
}



function increment($x , $max)
{
    $result = new RES();
    $result->value = $x + 1;
    if ($result->value == $max) 
    {
        $result->value=0;
        $result->bump_order = True;
    }
    return result;
}


function is_match($filter, $current)
{
    $result = False;
    return $result;
}




function next_match($filter, $current, $maxvalue)
{

    $tmp_bump_order = False;
    $tmp_res = new RES();
    
    if (($filter == "*") || ($filter == False))
    {
        // filter = "*"
        $tmp_res = increment($current , $maxvalue);
        if ($tmp_res.bump_order)
        {
            $tmp_bump_order = True;
        }
    }
    elseif






    
    elif re.match("\/\d+", filter) is not None:
        # filter = "/3"
        divider = int(re.search("\/(\d+)", filter).group(1))
        tmp_res = increment(current , maxvalue)
        x = tmp_res.value
        while tmp_res.value % divider != 0:
            tmp_res = increment(x , maxvalue)
            if tmp_res.bump_order:
                tmp_bump_order = True
            x = tmp_res.value
    
    elif re.match("\d+(?:,\d+)+", filter) is not None:
        # filter == "5,10,15"
        str_arr = re.search("\d+(,\d+)+", filter).group(0)
        arr = str_arr.split(",")
        for i in range(0, len(arr)):
            arr[i] = int(arr[i])
        
        tmp_res = increment(current , maxvalue)
        x = tmp_res.value
        while not(tmp_res.value in arr):
            tmp_res = increment(x , maxvalue)
            if tmp_res.bump_order:
                tmp_bump_order = True
            x = tmp_res.value
    
    elif re.match("(\d+)-(\d+)", filter) is not None:
        # filter == "9-18":
        fromint = int(re.search("(\d+)-(\d+)", filter).group(1))
        toint = int(re.search("(\d+)-(\d+)", filter).group(2))

        tmp_res = increment(current , maxvalue)
        x = tmp_res.value
        while not((tmp_res.value >= fromint) and (tmp_res.value <= toint)):
            tmp_res = increment(x , maxvalue)
            if tmp_res.bump_order:
                tmp_bump_order = True
            x = tmp_res.value

    tmp_res.bump_order = tmp_bump_order
    return tmp_res

}
















$a = new RES();
print("START");
var_dump($a->value);
var_dump($a->bump_order);