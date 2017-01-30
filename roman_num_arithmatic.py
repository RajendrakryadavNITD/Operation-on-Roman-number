import math
import  Roman_num_convertor
class RomanNumConvertor(object):
    def main_output_fun(self):
        try:
            input_first_roman_num = raw_input('Enter first Roman numeral :')
            input_second_roman_num = raw_input('Enter second Roman numeral :')
            operator = raw_input('choose which operation do you want to perform :')
            int_data_for_roman_conversion = self.do_arithmetic_operation(input_first_roman_num, input_second_roman_num, operator)
            Final_output = self.convert_integer_to_roman(int_data_for_roman_conversion)
            print 'Output is :' + Final_output
        except:
            raise
    def conert_roman_to_num(self, input_roman_num):
        try:
            if input_roman_num.isalpha() is True :
                roman_num_input_list = list(input_roman_num.upper())
                length_of_list = len(roman_num_input_list)
                roman_num_integer_num_dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
                result_integer_num = 0
                count = 0
                while(count < length_of_list):
                    num2 = 0
                    num1 = roman_num_integer_num_dict.get(roman_num_input_list[count],None)
                    if count <length_of_list-1 :
                        num2 = roman_num_integer_num_dict.get(roman_num_input_list[count+1],None)
                    else:
                        num2 = roman_num_integer_num_dict.get(roman_num_input_list[count],None)
                    if num1 is not None and num2 is not None:
                        if num1 >= num2 :
                            result_integer_num+=num1
                        else:
                            result_integer_num+= (num2-num1)
                            count+=1
                        count+=1
                    else:
                        result_integer_num = None
                        break
                return  result_integer_num
            else:
                return 'Input should be a capital Roman numerals'
        except:
            raise

    def do_arithmetic_operation(self, input_first_roman_num, input_second_roman_num, operator):
        try:
            result = 0
            operator = str(operator)
            first_integer_num = self.conert_roman_to_num(input_first_roman_num)
            second_integer_num = self.conert_roman_to_num(input_second_roman_num)
            if first_integer_num is not None and second_integer_num is not None:
                if operator== '+':
                    result = first_integer_num + second_integer_num
                elif operator== '-':
                    if first_integer_num > second_integer_num :
                        result = first_integer_num - second_integer_num
                    else:
                        print 'invalid operation'+ '\n' +'First roman number should be greater then second'
                elif operator == '*':
                    result = first_integer_num * second_integer_num
                elif operator == '/':
                    if first_integer_num < second_integer_num :
                        print 'invalid operation'+ '\n' +'First roman number should be greater then second'
                    else:
                        if first_integer_num % second_integer_num == 0:
                            result = first_integer_num / second_integer_num
                        else:
                            print 'invalid operation'+ '\n' +'It is not allowed in Roman number system'
                else:
                    print 'Enter a valid operator'
                return result
            else:
                return 'wrong input \n Enter a valid roman number'
        except:
            raise

    def convert_integer_to_roman(self, input_int_num):
        try:
            Integer_num_roman_num_dict = {1:'I', 4:'IV',5:'V',9:'IX',10:'X',40:'XL',50:'L',
                                          90:'XC',100:'C',400:'CD',500:'D',900:'CM',1000:'M'}
            if input_int_num > 0 and input_int_num < 4000:
                Roman_Numeral_list = []
                Roman_Numeral_reverse_list = []
                count = 0
                while(input_int_num):
                    num = input_int_num % 10
                    if num > 5:
                        value = int(math.pow(10, count))
                        Roman_Numeral = Integer_num_roman_num_dict.get(num*value, None)
                        if Roman_Numeral is not None:
                            Roman_Numeral_list.append(Roman_Numeral)
                        else:
                            value = int(math.pow(10, count))
                            num = num - 5
                            str_list = []
                            while (num) :
                                dict_value = int(math.pow(10, count))
                                Roman_Numeral = Integer_num_roman_num_dict.get(dict_value, None)
                                str_list.append(Roman_Numeral)
                                num = num - 1
                            list_to_str = "".join(str_list)
                            Roman_Numeral_list.append(list_to_str)
                            Roman_Numeral = Integer_num_roman_num_dict.get((5 * value), None)
                            Roman_Numeral_list.append(Roman_Numeral)
                        count += 1
                    else:
                        value = int(math.pow(10, count))
                        Roman_Numeral = Integer_num_roman_num_dict.get(num*value, None)
                        if Roman_Numeral is not None:
                            Roman_Numeral_list.append(Roman_Numeral)
                        else:
                            str_list = []
                            while (num):
                                value = int(math.pow(10, count))
                                Roman_Numeral = Integer_num_roman_num_dict.get(value, None)
                                str_list.append(Roman_Numeral)
                                num = num - 1
                            list_to_str = "".join(str_list)
                            Roman_Numeral_list.append(list_to_str)
                        count += 1
                    input_int_num = input_int_num / 10
                length = len(Roman_Numeral_list)
                while(length):
                    Roman_Numeral = (Roman_Numeral_list[length - 1])
                    Roman_Numeral_reverse_list.append(Roman_Numeral)
                    length = length - 1
                Final_Roman_Numeral ="".join(Roman_Numeral_reverse_list)
                return Final_Roman_Numeral
            else:
                return 'Operation should be in range of I to MMMCMXCIX is only possible'
        except:
            raise